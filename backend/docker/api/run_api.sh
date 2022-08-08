#!/bin/bash

export $(cat .env | xargs)

until pg_isready -q -p 5432 -h ${CONTAINER_NAME}'_db' -U ${POSTGRES_USER};
do
    echo "Waiting for Postgres"
    sleep 2;
done;
echo "Connected"
cd app && python3 run.py