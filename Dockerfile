# Use a lightweight Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy your requirements and solver
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY solver.py .

# Run the solver when the container starts
CMD ["python", "solver.py"]
