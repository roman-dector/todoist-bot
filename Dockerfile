FROM python:3.10.0-slim-buster

WORKDIR /todoist_bot

COPY requirements.txt requirements.txt 

RUN pip3 install -r requirements.txt 

COPY . .

CMD ["python3", "todoist_bot/run_bot.py"]
