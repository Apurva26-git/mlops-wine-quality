FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy everything including templates
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]