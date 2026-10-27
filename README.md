# Market Tracker API

A REST API for crowdsourced crop prices across Ethiopian markets. Suppliers, merchants and buyers can all see what a crop is selling for in different markets, which reduces the information gap between them.

Frontend repo: https://github.com/surafeladane/market-tracker-web

## Why I built this

WRITE 3-4 SENTENCES IN YOUR OWN WORDS HERE.

## Features

- Crops, markets and price entries, linked with foreign keys
- Token-based login and sign-up
- Anyone can read prices; only logged-in users can submit them
- The server sets the submitting user from the login token, so one user can't post under another's name

## Tech stack

Python, Django, Django REST Framework, SQLite, django-cors-headers

## Run it locally

```
python -m pip install django djangorestframework django-cors-headers
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The API runs at http://127.0.0.1:8000/api/. Add a few crops and markets through the admin panel at /admin/.

## What I'd build next

- Price trend charts per crop and market
- Moderation for bad or spam price entries
- Support for more regions and units