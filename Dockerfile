# Use the official lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Set the PYTHONPATH so Python can find your modules
ENV PYTHONPATH=/app

# Default command to run tests (can be overridden)
CMD ["pytest", "tests/smoke/test_sample.py", "-s"]