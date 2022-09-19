import argparse
import os
import subprocess
import sys
from copy import deepcopy
from enum import Enum
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

DOCKER_COMPOSE_NAME = "docker-compose.yml"
DOCKER_COMPOSE_DEV_NAME = "docker-production.yml"


class Command(Enum):
    CONFIG = "config"
    UP = "up"
    STOP = "stop"
    INIT = "init"
    BUILD = "build"
    DOWN = "down"
    RESTART = "restart"


arg_parser = argparse.ArgumentParser(
    description="Cities wishlist instance management")

def execute_bash(args: List[str], envs=None) -> Tuple[int, bytes, bytes]:
    envs = envs or {}
    result_envs = deepcopy(os.environ)
    result_envs.update(envs)
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=result_envs)
    return result.returncode, result.stdout, result.stderr

def exec_docker_compose(args, envs=None, remain=False):
    envs = envs or {}
    result_envs = os.environ
    result_envs.update(envs)

    args.insert(0, "docker-compose")
    remain = True
    execute_bash(args, result_envs)
    

def main():
    args, extra_args = arg_parser.parse_know_args()
    dev = not bool


if __name__ == "__main__":
    result = main()
    sys.exit(result)
