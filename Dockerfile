FROM python:3.9-slim

WORKDIR /app

# Copy everything (make sure model.joblib is present when building)
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]