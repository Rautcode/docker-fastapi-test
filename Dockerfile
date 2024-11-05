FROM python:3.9
WORKDIR /app
COPY app /app/app
RUN pip install fastapi uvicorn
RUN mkdir -p /app/app/data && chmod -R 777 /app/app/data
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
