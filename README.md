## Instalation
clone this repo

`git clone https://github.com/Blucknote/tgbot/`

## Using
### Configuration

[obtain token for your bot](https://core.telegram.org/bots/api#authorizing-your-bot)

Make a conf.yml file looking like this
```
token:
  "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11" 
debugch:
  0       # Using for redirecting bot answers. Can be user id or @channel
webhook:
  True    # if you want use webhooks you need this part
domain:   # otherwise you can skip this part. Wrapper support polling
  "https://your.domain/"
ssl:
  "/etc/letsencrypt/live/your.domain/cert.pem" # path may be different
```

### Code
```
import tgbot
@tgbot.on_message(r'^/start\s?.*')
def hello(message):
    tgbot.send_message(message['from']['id'], 'Hello!')
```