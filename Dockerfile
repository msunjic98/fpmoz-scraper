FROM python:latest

WORKDIR /usr/src/app

COPY main.py /usr/src/app
COPY sources.json /usr/src/app
COPY sources.py /usr/src/app
COPY ObavijestiAPI.py /usr/src/app
COPY ObavijestiModel.py /usr/src/app

RUN pip install --upgrade pip
RUN pip install beautifulsoup4
RUN pip install flask
EXPOSE 5050
ENV FLASK_APP main.py
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "5050"]