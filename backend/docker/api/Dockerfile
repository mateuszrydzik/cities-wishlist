FROM python:3.9
RUN apt-get update
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY ./run_api.sh /run_api.sh
RUN chmod +x /run_api.sh