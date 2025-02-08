FROM python:3.9

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y default-mysql-client && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the wait script
COPY scripts/wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh

# Copy the rest of the application
COPY . .

# Command to run the application with wait script
CMD ["/wait-for-db.sh", "db", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
