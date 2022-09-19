# Cities wishlist

### Find all the cities you ever wished to visit. 

Easy to use app that helps you plan your future trips. 
Mark your travel destination on the map with a single click. City's name will be automatically saved! Add notes to your markers and access it's information in a pop-up.

_Docker required_

## Setup
### Create .env file containing:
```sh
CONTAINER_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DBNAME=
DB_PORT=
NGINX_PORT=
SECRET_KEY=
```
### Run Docker containers
```sh
docker compose up 
```
if it's the first time, run
```sh
docker compose up --build
```

## Usage
* To access client:
localhost:{NGINX_PORT}

* To access documentation:
localhost:{NGINX_PORT}/api/docs
