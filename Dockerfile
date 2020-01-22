#https://raw.githubusercontent.com/Docker-Hub-frolvlad/docker-alpine-python3/master/Dockerfile
FROM node:lts-alpine

ENV PYTHONUNBUFFERED=1

RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    rm -rf /var/cache/apk/* && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel virtualenv pytest pytest-bdd && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PROFILE $PROFILE

WORKDIR /app
# RUN pytest-bdd generate test/feature/establish_environment.feature > test/step_defs/establish_environment.py && cp test/step_defs/establish_environment.py /opt/use_chromeos

# Install dependencies:
COPY pytest-bdd_cli.py requirements.txt /app/
RUN pip install -r requirements.txt

# Run the application:
ENTRYPOINT ["python3", "pytest-bdd_cli.py"]
