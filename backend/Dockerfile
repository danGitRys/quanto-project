# Base image

FROM python:3.12.0

# Install ODBC Driver 17 for SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get -y install msodbcsql17

# Setup environment variables
ENV DockerHOME=/home/app/webapp

# Set work directory
RUN mkdir -p $DockerHOME
WORKDIR $DockerHOME

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip

# Copy the entire project to the Docker home directory
COPY . $DockerHOME

# Run this command to install all dependencies
RUN pip install -r requirements.txt

# Expose the port where the Django app runs
EXPOSE 8000

# Start the server
CMD python manage.py runserver 0.0.0.0:8000