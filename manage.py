import argparse
import os
import subprocess
import sys
from copy import deepcopy
from enum import Enum
from pathlib import Path
from typing import Dict, Optional, List, Tuple

import manage_config_template


CONFIG_LOADED = False
CONFIG = {}
CONFIG.update(manage_config_template.config)

try:
    import manage_config
    CONFIG_LOADED = True
    CONFIG.update(manage_config.config)
except ImportError as e:
    print(e)

DOCKER_COMPOSE_NAME = "docker-compose.prod.yml"
DOCKER_COMPOSE_DEV_NAME = "docker-compose.yml"

IS_WINDOWS = os.name == 'nt'

class Command(Enum):
    CONFIG = "config"
    UP = "up"
    STOP = "stop"
    BUILD = "build"
    DOWN = "down"
    RESTART = "restart"

arg_parser = argparse.ArgumentParser(description="Cities wishlist instance management")
arg_parser.add_argument("--prod", dest="prod", action="store_true", help="Uruchomienie w trybie produkcyjnym.")
subparsers = arg_parser.add_subparsers(title="Dostępne polecenia", dest="command")

parser_config = subparsers.add_parser(Command.CONFIG.value, help="Wyświetla docelowe zmienne środowiskowe")
parser_up = subparsers.add_parser(Command.UP.value, help="Podniesienie kontenerów (docker-compose up)")
parser_stop = subparsers.add_parser(Command.STOP.value, help="Zatrzymanie kontenerów (docker-compose stop)")
parser_restart = subparsers.add_parser(Command.RESTART.value,
                                       help="Restart kontenerów (docker-compose restart) lub wybranych serwisów (docker-compose restart geoserver database)")
parser_up.add_argument("--build", dest="build", action="store_true", help="Wykonuje build kontenerów")
parser_up.add_argument("-d", dest="daemon", action="store_true", help="Podnosi kontenery w tle")

parser_build = subparsers.add_parser(Command.BUILD.value, help="Wykonuje build kontenerów (docker-compose down)")
parser_down = subparsers.add_parser(Command.DOWN.value, help="Zatrzymuje kontenery, usuwa kontenery, sieci, wolumeny i obrazy (docker-compose down)")

def print_missing_config_warning():
    print("nie znaleziono pliku konfiguracyjnego manage_config.py")
    print("zostaną użyte domyślne zmienne środowiskowe z pliku .env")



def execute_bash(args: List[str], envs=None) -> Tuple[int, bytes, bytes]:
    envs = envs or {}
    result_envs = deepcopy(os.environ)
    result_envs.update(envs)
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=result_envs)
    return result.returncode, result.stdout, result.stderr

def execute_bash_foreground(args: List[str], envs=None):
    envs = envs or {}
    result_envs = deepcopy(os.environ)
    result_envs.update(envs)
    p = subprocess.Popen(args, env=result_envs)
    p.wait()
    return p.returncode

def printArgs(args):
    print('`' + ' '.join(args) + '`')

def exec_docker_compose(args, envs=None, remain=False):
    envs = envs or {}
    result_envs = os.environ
    result_envs.update(envs)

    args.insert(0, "docker-compose")
    printArgs(args)
    remain = True
    if remain or IS_WINDOWS:
        return execute_bash_foreground(args, result_envs)
    else:
        execute_bash(args, result_envs)
    
def exec_docker(container_name: str, interactive: bool, command: str, args=None):
    args = args or []
    result_args = ["docker", "exec"]
    if interactive:
        result_args.append("-it")

    result_args.extend([container_name, command])
    if args:
        result_args.extend(args)
        execute_bash(result_args)

def get_docker_compose_args(dev: bool):
    args = ["-f", DOCKER_COMPOSE_NAME]

    if dev:
        args.extend(["-f", DOCKER_COMPOSE_DEV_NAME])

    local_composes = CONFIG["local_docker_composes"]
    for local_compose in local_composes:
        args.extend(["-f", local_compose])

    return args

def get_envs_override() -> Dict:
    if CONFIG_LOADED is False:
        return {}

    envs_override = CONFIG["envs_override"]
    return envs_override

def get_envs(with_override=False) -> Dict:
    file = Path(".env")
    result = {}

    content = file.read_text()
    lines = content.split("\n")
    for line in lines:
        line = line.strip()
        if line == "":
            continue

        if line.startswith("#"):
            continue

        if "=" in line:
            key, value = line.split("=", maxsplit=1)
            result[key] = value

    if with_override:
        result.update(get_envs_override())

    return result

def up(dev: bool, build_: bool, daemon: bool, remain=False):
    args = get_docker_compose_args(dev)

    args.append("up")

    if build_:
        args.append("--build")

    if daemon:
        args.append("-d")

    envs = get_envs(True)

    exec_docker_compose(args, envs, remain)

def stop(dev: bool, remain=False):
    args = get_docker_compose_args(dev)
    args.append("stop")
    exec_docker_compose(args, remain=remain)

def build(dev: bool, remain=False):
    args = get_docker_compose_args(dev)
    args.append("build")
    envs = get_envs(True)
    return exec_docker_compose(args, envs, remain)

def down(dev: bool, remain=False):
    args = get_docker_compose_args(dev)
    args.append("down")
    exec_docker_compose(args, remain=remain)

def restart(services_names: Optional[List] = []):
    args = get_docker_compose_args(False)
    args.append('restart')
    args.extend(services_names)
    exec_docker_compose(args)

def config():
    envs = get_envs(True)
    for k, v in sorted(envs.items()):
        print(f"{k}={v}")

def main():
    args, extra_args = arg_parser.parse_known_args()
    dev = not bool(args.prod)

    command = Command(args.command)
    if command == Command.CONFIG:
        config()
        if CONFIG_LOADED is False:
            print_missing_config_warning()
        sys.exit()

    if CONFIG_LOADED is False:
        print_missing_config_warning()

    if command == Command.UP:
        up(dev, bool(args.build), bool(args.daemon))

    if command == Command.STOP:
        stop(dev)

    if command == Command.BUILD:
        build(dev)

    if command == Command.DOWN:
        down(dev)

    if command == Command.RESTART:
        restart(extra_args)

if __name__ == "__main__":
    result = main()
    sys.exit(result)
