# Start with a lightweight Python Linux system
FROM python:3.10-slim

# Set the working folder inside the container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your actual code
COPY . .

# Tell Docker to open port 8000
EXPOSE 8000

# The command to run when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]