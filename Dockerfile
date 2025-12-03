# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project
COPY . .

# Expose port if needed (e.g., for web apps)
EXPOSE 8000

# Default command to run your app
CMD ["python", "hello_world.py"]



