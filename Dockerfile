# Use an official Python base image
FROM python:3.10.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Django runs on
EXPOSE 8000

# Run migrations and start the Django app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "Sydney_Backend.wsgi:application"]
