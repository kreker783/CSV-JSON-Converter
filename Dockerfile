FROM python:3.11
WORKDIR /app
ENV FLASK_RUN_HOST=0.0.0.0
COPY code/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY code/. .
EXPOSE 5000
CMD [ "flask", "run", "--debug" ]
