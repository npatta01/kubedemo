# Which bash image/os are you starting "From"
From ubuntu:16.04

# "Run" this command to setup 
RUN apt-get update && apt-get install -y --no-install-recommends  \
        python3-setuptools \
        python3 \
        python3-pip

# Create a folder and set this as your working directory
WORKDIR /my_app

# "Copy" file to working dir
COPY requirements.txt .

# "Run" command that installs dependencies
RUN pip3 install -r requirements.txt

# Copy all files to working dir
COPY . .

# Set "env" variables
ENV PORT 5000
ENV CREATOR anonymous-docker

# Which port should the container listen on
EXPOSE $PORT

# When the container runs what command should it run
ENTRYPOINT ["/bin/bash", "-c", "python3 app.py"]
 
