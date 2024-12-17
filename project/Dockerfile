# Use the official Python image as the base image
FROM python:3.12.5


# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app


# Install dependencies
RUN pip install --no-cache-dir flask


# Expose the port Flask will run on
EXPOSE 5000

# Define the command to run the application
# CMD ["python", "app.py"]

CMD python ./app.py 

