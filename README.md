## Install
clone this repo

`git clone https://github.com/Blucknote/tgbot/`

## Config

[obtain token for your bot](https://core.telegram.org/bots/api#authorizing-your-bot)

Make a conf.yml file looking like this
```
token:
  "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11" 
debugch:
  0       # Unnecesary. Using for redirecting bot answers. Can be user id or @channel
webhook:
  True    # Set this to True if you want to. If not polling will be used instead
# below this comment using for webhooks support. You can skip if polling.
domain:  
  "https://your.domain/"
ssl:
  "/etc/letsencrypt/live/your.domain/cert.pem" # path may be different
```

## Run
```python
from tgbot import event_listener
from tgbot import events
from tgbot import tgapi

@events.on_message(r'^/hello$')
def hello(message):
    tgapi.send_message(message['from']['id'], 'Hello!')

event_listener.message_handlers.extend((hello,))
event_listener.start(r'conf.yml')
```
