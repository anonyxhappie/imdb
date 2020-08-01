# IMDB
This project is aimed to create a RESTful API for movies(something similar to IMDB). And a decent implementation to search for movies having 2 levels of access:
admin = who can add, remove or edit movies.
users = who can just view the movies.

# Technologies used
- [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
- [DRF](https://www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs.
- [Django-Filter](https://django-filter.readthedocs.io/en/stable/): It allows users to filter down a queryset based on a model’s fields.
# Docker images used
- [frolvlad/alpine-python3](https://hub.docker.com/r/frolvlad/alpine-python3) - for base image

# Prerequisites
- Install Docker
> $ curl -fsSL https://get.docker.com -o get-docker.sh
> $ sudo sh get-docker.sh
- Install Git
> $ sudo apt install git

# Installation
- Clone repo & cd to project directory
> $ git clone https://github.com/anonyxhappie/imdb.git; cd imdb
- Run start up script
> $ bash -e start.sh


# Movie API
- Example request for Movie Listing
```
curl -X GET \
  http://localhost:8000/movies/ \
  -H 'authorization: Basic YWRtaW46YWRtaW4='
```
- Example response
```
{
    "count": 496,
    "next": "http://localhost:8000/movies/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "genre": [
                "Musical",
                "Family",
                "Adventure",
                "Fantasy"
            ],
            "name": "The Wizard of Oz",
            "director": "Victor Fleming",
            "imdb_score": 8.3,
            "popularity": 83
        },
        {
            "id": 2,
            "genre": [
                "Action",
                "Adventure",
                "Sci-Fi",
                "Fantasy"
            ],
            "name": "Star Wars",
            "director": "George Lucas",
            "imdb_score": 8.8,
            "popularity": 88
        },
	...
	]
}
```

# Admin UI
- open below link in browser to access Admin UI
> http://localhost:8000/admin/
- Login using credentials given in settings.ini
- Create normal user who can just GET movie details 

# DRF Web Browsable API
- Open http://localhost:8000 in browser
- Get movie list at http://localhost:8000/movies/
- Get single movie detail at http://localhost:8000/movies/1/
- Login by admin for updating movie details
- Browsable API UI helps to play around with API (try different search filters)

# Scalability
Once deployed suppose this application became very famous and started to receive
a ton of traffic. Your application now contains metadata about 5M movies and
receives 15M API hits per day both from anonymous as well as authenticated users.
Suggest an architecture to scale up this system to 5x of these specs.

- Very first we need to replace the file based DB (sqlite3) to Production Level DB (MySQL/Postgres)
- We would need to add caching mechanism (Redis/Memcached) for handling large number of requests (It'll help fetch data faster without interacting with DB)
- We will add a sync to caching mechanism to update cache from DB by TTL at cache or write event on DB
- We will create DB replication for better accessibility for read & write operations saperately & for better accessiblity 
- We will have to set up a load balancer for scalling up the api & db servers
- We can set throttling to limit requests by user/day 
