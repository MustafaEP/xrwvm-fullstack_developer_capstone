FROM python:3.12.0-slim-bookworm

ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYTECODE=1
ENV APP=/app

# Change the working directory
WORKDIR $APP

# Copy requirements file
COPY requirements.txt $APP

# Install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy the rest of the application code
COPY . $APP

# Expose port
EXPOSE 8000

# Make entrypoint executable
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
