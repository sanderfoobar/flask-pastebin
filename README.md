flask-pastebin
============

A pastebin.com/pastie.org clone based on `flask`.

![Alt text](http://i.imgur.com/9Ij8vU3.png "Example")

Live example can be found [here](http://paste.cedsys.nl "cedsys").

## Features

- Paste expiration
- Syntax highlighting
- A sidebar with recent (public) pastes
- Filesystem based - so no database required

## Installation

    $ apt-get install libevent-dev python-dev python-virtualenv python-pip
    
    $ virtualenv paste_service
    $ cd $_
    $ git clone https://github.com/skftn/flask-pastebin.git
    $ source bin/activate
    $ cd flask-pastebin/
    $ pip install -r requirements.txt
    $ python paste.py


## Disclaimer

Coded in 5 hours; the mileage you get out of this may vary.

