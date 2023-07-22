FROM python:3.11
WORKDIR /app
COPY code/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "flask", "run", "--debug" ]
