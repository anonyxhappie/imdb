# set the base image 

FROM frolvlad/alpine-python3

# create working directory

RUN mkdir -p /imdb/imdb_project

# create directory to mount

RUN mkdir -p /tmp/imdbfiles

# set directoty where CMD will execute 

WORKDIR /imdb/imdb_project

# add project files to the /imdb/imdb_project folder

COPY imdb_project ./

# add settings.ini file

COPY settings.ini /imdb/

# add requirements.txt file

COPY requirements.txt ./

COPY sample.json /imdb/

# get pip to download and install requirements:

RUN pip install --no-cache-dir -r requirements.txt

# Create DB Schema 

RUN python3 /imdb/imdb_project/manage.py migrate

# Create superuser (admin) 

RUN python3 /imdb/imdb_project/manage.py initadmin

# Add default rules in DB 

RUN python3 /imdb/imdb_project/manage.py preparedb

# Expose ports

EXPOSE 8000

# default command to execute      

CMD python3 /imdb/imdb_project/manage.py runserver --insecure 0.0.0.0:8000