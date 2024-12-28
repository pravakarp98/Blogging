FROM python:3.9
RUN apt update && apt upgrade -y
RUN apt install -y cron vim redis nano supervisor
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app /app
# Copy the supervisor configuration file
COPY supervisord.ini /etc/supervisor/conf.d/consumer_supervisor.conf
COPY supervisord.conf /etc/supervisor/supervisord.conf
RUN chmod 777 entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]