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
This information is in the StarWars Public API: https://swapi.co/.
It's also required a CRUD: add planet, list planets, search by name, search by id and remove planets.

## What have I done

As per my choice, I'm using Python, Flask and MongoDB to create this API.
The source code will be available at [github](https://github.com/phasath/b2w-starwars-challenge) and
it'll be online in [heroku](https://b2w-starwars-challenge.herokuapp.com/).

# Instalation

## Requirements 
- [pipenv](https://pipenv.readthedocs.io/en/latest/install/)
- [Python 3.7.2](https://www.python.org/downloads/release/python-372/)
- [MongoDB](https://www.mongodb.com/)

## Installing

If you're using it as development mode, then, you may change some settings to use your local mongo database.
You can do that exporting your mongo db uri to an env var `MONGODB_URI` or you can change the `settings.py` file.

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