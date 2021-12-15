FROM python:3.9-slim

# SSH password
ENV SSH_PASSWD "root:Docker!"

WORKDIR /app

COPY . /app/
COPY sshd_config /etc/ssh/

# gcc/libpq-dev/python3-dev need to be installed prior to requirements.txt being installed so psycopg2 can compile
RUN apt-get update -yy \
    && apt-get upgrade -yy \
    && apt-get install gcc libpq-dev python3-dev -yy \
    && pip install -r requirements.txt \
    && python manage.py collectstatic --noinput \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "$SSH_PASSWD" | chpasswd \
    && chmod +x /app/init_container.sh

EXPOSE 8000 2222

ENTRYPOINT [ "/app/init_container.sh" ]
