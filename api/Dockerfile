# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# This image comes with root as default user.
# For best practices and security reasons, we never should run a container as root.
# Create a group and a new user to with.
RUN adduser --disabled-password --gecos app python

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the dependencies
RUN pip install -r requirements/requirements.txt

# set user python
USER python

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
