Django Twitter Clone
====================

This repo is my attempt at a small and simple Twitter "clone" using Django.
It's a clone in name only, since I'm not actually copying their REST API or web
interface.  I'm just making a site with similar REST API and functionality.

To achieve this, I'm using the Django REST Framework to create a REST API
backend, and then I'll later create a frontend website using Javascript.


Setup
-----

Right now it's simple.  (Requires Linux, Python 3, etc.)

```bash
$ git clone git@github.com:brenns10/dtwit.git
$ cd dtwit
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ ./manage.py createsuperuser  # (you'll want this)
$ ./manage.py runserver
```

Then head to <http://localhost:8000/tweets> to start playing with the REST API.
