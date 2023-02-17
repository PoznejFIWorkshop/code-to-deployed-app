FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# This would work on your PC, but not in Docker. The --host=0.0.0.0 is the key.
# CMD ["python3", "app.py"]

# This is the proper way how to start Flask (but still not the best way).
ENV FLASK_APP app.py
CMD [ "flask", "run", "--port=80", "--host=0.0.0.0"]
