# Use the specific version tag for the Python image
FROM python:3.11.4-slim-buster

# Prevent Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
# Ensure that Python outputs everything that's printed inside the application rather than buffering it
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /core

# Upgrade pip and install dependencies
COPY requirements.txt /core/
RUN pip install --upgrade pip && pip install -r requirements.txt


# Install vim (if needed, you can remove this line if not necessary)
RUN apt-get update && apt-get install -y vim && rm -rf /var/lib/apt/lists/*

# Copy the application code into the container
COPY . /core/

# Expose the port your app runs on
EXPOSE 8000

# Specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
