# Star Wars B2W Challenge

Summary: An API regarding the planets information created for a challenge proposed by B2W

Author: Raphael Sathler

Home-page: www.raphaelsathler.tk

Author-email: sathler93@gmail.com

License: GNU GPL v3.0

## Why?

This is a job interview challenge. B2W people are very into Star Wars. So they created a challenge about it!

## Challenge Requirements

A REST API should be created to serve the Name, Wheather and Surface of each Planet from Star Wars.
It's also desirable to know how many movies did that planet appeared.
This information is in the [StarWars Public API](https://swapi.co/).
It's also required a CRUD: add planet, list planets, search by name, search by id and remove planets.

## What is this?

I'm using Python, Flask and MongoDB to create this API.
The source code will be available at [github](https://github.com/phasath/b2w-starwars-challenge) and
it'll be online in [heroku](https://b2w-starwars-challenge.herokuapp.com/).

## Useful Information

### StarWars API

The API doesn't keep data from the StarWars API in the database so, it will always have the most updated information about the planets.
Having this in mind, it uses a cache with a time to die of 300s to avoid be constantly making requests from StarWars API.

### Indexes

It also creates a index on the collections used (`planets`) to allow faster queries on planet names.

### Error Messages

It creates a function to return error messages more humanized along with the error code.

### App Factory Format

It uses the APP Factory format to start flask applications.

### Flask Restful

It is using the Flask Restful package to allow better use of the HTTP verbs and implementation.

### Extensions

It is also using Extensions to keep everything that is used wide-spreadly on the API imported from the same place, avoiding misleading configuration.

### Settings

All the configurations regarding this API is found under the `settings.py` file and they can also be overwritten using `environment variable`.

### Tests

All the routes are tested and there's also a coverage report.htmlcov

# Instalation

## Requirements 
- [pipenv](https://pipenv.readthedocs.io/en/latest/install/)
- [Python 3.7.2](https://www.python.org/downloads/release/python-372/)
- [MongoDB](https://www.mongodb.com/)

## Installing

### MongoDB

If you're using it as development mode, then, you may change some settings to use your local mongo database.
You can do that exporting your mongo db uri to an env var `MONGODB_URI` or you can change the `settings.py` file.

If you don't have a user, you can, as long as your mongodb instance is in localhost or you have authorized access without login and password; use the script to create a user `obi_wan` and password `kenobi` to access the database.
To do so, use:
```
$ pipenv run setup_mongo
```

If you want to run tests, please, setup mongo with the test instance, where user is `chewbacca` and password `GGGWARRRHHWWWW` or use:

```
$ pipenv run setup_test_mongo
```

### Python

Pretty simple, just use pipenv to install all dependencies:

```
$ pipenv install
```

If you'd like to enter on the virtual env generated:

```
$ pipenv shell
```

Or, you can simply run the API using:

- For Development

```
$ pipenv run dev
```

- For Production

```
$ pipenv run start
```

## Other Commands:

Run the linter: 

```
$ pipenv run lint
```

Run the Tests:

```
$ pipenv run tests
```

# API Endpoints

## JSON Response Example:

```
{
    "id":"ab739d11e8df48df67ae1a9b",
    "name":"Yavin IV",
    "climate":"temperate, tropical",
    "terrain":"jungle, rainforests",
    "apparitions_count":1
}
```

## GET /api/planets

**Description:** Returns all planets from database

**Response Code:** 
- 200 when success.
- 204 when theres no data.

**Response Data:** Json with planets.


## GET /api/planets/{planet_id}

**Description:** Searchs for a planet using it's id.

**Response Code:** 
- 200 when success.
- 204 when theres no data.

**Response Data:** Json with planets.


## GET /api/planets/name/{planet_name}

**Description:** Searchs for a planet using it's name.

**Response Code:**
- 200 when success.
- 204 when theres no data.

**Response Data:** Json with planets.


## POST /api/planets/

**Description:** Inserts a new planet

**Response Code:** 
- 201 when success.
- 422 when no data is sent on the post.
- 409 when the planet alerady exists.
- 403 when the planet was not found on star wars api.

**Response Data:** Json with the created planet.


## PUT /api/planets/{planet_id}

**Description:** Updates a planet info

**Response Code:** 
- 200 when success.
- 422 when no data is sent on the post.
- 204 when planet id didn't match on db

**Response Data:** Json with the updated planet.

## DELETE /api/planets/{planet_id}

**Description:** Deletes a planet using it's id.

**Response Code:** 
- 204 when success.
- 422 when no planet id.

**Response Data:** An empty list `[]`

## DELETE /api/planets/delete/{planet_name}

**Description:** Deletes a planet using it's name

**Response Code:** 
- 204 when success.
- 422 when no planet name.

**Response Data:** An empty list `[]`