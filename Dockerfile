FROM python:3.8-slim


# set working dir
WORKDIR /app

# copy all requirments
# if new requirements are added, use 
# pip freeze > requirements.txt
COPY requirements.txt .

# install all requirements
RUN pip install --no-cache-dir -r requirements.txt

# ? 
COPY . .

# run app on this port
EXPOSE 5000


# `python3 app/bot.py'
# setting the working dir should let this just be `python3 bot.py'
# but for whatever reason it doesn't
CMD [ "python3", "app/bot.py" ]