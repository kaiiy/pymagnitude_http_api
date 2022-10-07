FROM python:3.9-bullseye

RUN pip3 install pymagnitude

RUN pip3 install fastapi uvicorn

EXPOSE 8080