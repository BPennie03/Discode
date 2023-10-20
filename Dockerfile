FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# run app on this port ig
EXPOSE 5000

CMD [ "python3", "app/bot.py" ]