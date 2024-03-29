FROM python:3.7.9

RUN mkdir -p /home/app

# create the app user
RUN addgroup app && adduser --system --no-create-home app --ingroup app

# create the appropriate directories
ENV HOME=/home/app

ENV APP_HOME=/home/app

WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

COPY . $APP_HOME

RUN curl https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5 -O -J -L

RUN mv yolo.h5 ${APP_HOME}/model/yolo.h5 

RUN pip freeze > requirements.txt

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

ENTRYPOINT ["python main.py"]