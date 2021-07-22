FROM python:3.7.9

RUN mkdir -p /home/app

# create the app user
RUN addgroup app && adduser --system --no-create-home app --ingroup app

# create the appropriate directories
ENV HOME=/home/app

ENV APP_HOME=/home/app/

WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

COPY . $APP_HOME

RUN pip install -r $APP_HOME/requirements.txt

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

ENTRYPOINT ["python main.py"]