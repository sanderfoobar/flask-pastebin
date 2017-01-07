flask-pastebin
============

A pastebin.com/pastie.org clone based on `flask`.

![Alt text](http://i.imgur.com/9Ij8vU3.png "Example")

Live example can be found [here](http://paste.cedsys.nl "cedsys").

## Disclaimer

Speedcoded, so code quality is shit (but should be secure).

## Features

- Paste expiration
- Syntax highlighting
- Image uploader (barely works)
- A sidebar with recent (public) pastes
- Filesystem based (no db)

## Installation

    $ apt-get install libevent-dev python-dev python-virtualenv python-pip
    
    $ virtualenv paste_service
    $ cd $_
    $ git clone https://github.com/skftn/flask-pastebin.git
    $ source bin/activate
    $ cd flask-pastebin/
    $ pip install -r requirements.txt
    $ python paste.py

## Paste screenshot from terminal with scrot, python-requests, libnotify, xclip

    $ sudo apt-get install python-requests, scrot, xclip, libnotify-bin, libnotify-dev

`/usr/bin/paste_screenshot_region.sh`:

```
#!/bin/bash
nohup echo $(scrot -s -e 'printf $f | python -c "\$\(echo aW1wb3J0IHN5cztpbXBvcnQgcmVxdWVzdHM7YmFzZV91cmkgPSAiaHR0cHM6Ly9wYXN0ZS5jZWRzeXMubmwiO2ZpbGVzID0geyJmaWxlc1tdIjogb3BlbihzeXMuc3RkaW4ucmVhZCgpKX07ciA9IHJlcXVlc3RzLnBvc3QoIiVzL3Bhc3RlIiAlIGJhc2VfdXJpLCBmaWxlcz1maWxlcyk7c3lzLnN0ZG91dC53cml0ZSgiJXMlcy9yYXciICUgKGJhc2VfdXJpLCByLmpzb24oKVsidXJpIl0pKQ== | base64 -d\)" && mv $f ~/screenshots') | xclip -selection clipboard && notify-send -t 1000 $(echo "Pasted (clipboard)") &
```

`chmod +x`. openbox keyboard shortcut (CTRL-printscreen):

```
    <keybind key="C-Print">
      <action name="Execute">
        <execute>paste_screenshot_region.sh</execute>
      </action>
    </keybind>

```

    $ openbox --reconfigure
