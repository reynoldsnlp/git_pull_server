FROM ubuntu:22.04

RUN apt-get update && apt-get install -y git python3 python3-pip

WORKDIR /app

COPY requirements.txt ./

RUN cd .. && pip install -r app/requirements.txt && cd app

COPY . .

EXPOSE 5000

# SCRIPT_NAME is used by gunicorn to add prefix to paths, e.g. 0.0.0.0:5055/git_pull_server
ENV SCRIPT_NAME=/git_pull_server

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5055", "--capture-output", "--log-level", "debug", "gps:app"]
