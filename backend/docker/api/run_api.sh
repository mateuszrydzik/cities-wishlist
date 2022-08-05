#!/bin/bash

export $(cat .env | xargs)

echo "Oczekiwanie na polaczenie"


 until docker run --rm --link ${CONTAINER_NAME}'_db':pg postgres:9.5 pg_isready -U ${POSTGRES_USER} -h ${CONTAINER_NAME}'_db'; 
 do 
    echo "Oczekiwanie na baze danych"
    sleep 1; 
done
sleep 2
echo "Polaczono"
cd app && python3 run.py

until pg_isready -q -p 5432 -h ${CONTAINER_NAME}'_db' -U ${POSTGRES_USER};
do
    echo "Oczekiwanie na baze danych"
    sleep 2;
done;
sleep 2
echo "Polaczono"
cd app && python3 run.py