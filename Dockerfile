FROM python:3.10

RUN mkdir -p /red_bot

WORKDIR /red_bot

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]