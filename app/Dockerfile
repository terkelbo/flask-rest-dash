FROM python:3.6

COPY . /app
RUN pip install -r app/requirements.txt

EXPOSE 80
CMD ["python", "/app/main.py"]