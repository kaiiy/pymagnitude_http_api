FROM python:3.9-bullseye

RUN pip3 install pymagnitude

RUN pip3 install fastapi uvicorn

EXPOSE 45200

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "45200"]