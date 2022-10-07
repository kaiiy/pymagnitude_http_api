FROM python:3.9-bullseye

RUN pip3 install pymagnitude

RUN pip3 install fastapi uvicorn

EXPOSE 8080

# CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"] 