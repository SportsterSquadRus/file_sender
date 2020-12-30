FROM python:3

RUN mkdir -p /usr/src/server_agent

WORKDIR /usr/src/server_agent

COPY . /usr/src/server_agent
RUN pip install --no-cache-dir -r /usr/src/server_agent/requirements.txt

EXPOSE 8000
