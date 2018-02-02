from urllib.request import urlopen, quote
import json

domain = 'https://api.telegram.org/bot%s/'

def read_token(_file):
    return json.loads(open(_file).read())

try:
    token = read_token('settings.json')['token']
except KeyError:
    raise ValueError('Cannot continue without token! Provide it')
else:
    if not token:
        raise ValueError('Token provided but its empty')

debugch = read_token('settings.json')['debugch']

def retry(fn):
    from time import sleep
    def wrapper(*args):
        retries = 10
        i = 0
        while i < retries:
            try:
                ret = fn(*args)
            except:
                i += 1
                sleep(3)
            else:
                return ret
    return wrapper

def set_webhook(self_domain_path: str, certificate):
    addr = {
        'api': domain % token,
        'method': 'setWebhook?',
        'url': 'url=%s' % self_domain_path,
        'cert': '&certificate=%s' % open(certificate, 'r'),         
    }
    return urlopen('{api}{method}{url}{cert}'.format(**addr))

@retry
def send_message(chatid, msg, reply_markup = ''):    
    addr = {
        'api': domain % token,
        'chatid': 'sendMessage?chat_id=%s' % chatid,
        'text': '&text=%s' % quote(msg),
        'reply': '&reply_markup=%s' % reply_markup        
    }
    
    return urlopen('{api}{chatid}{text}{reply}'.format(**addr))

@retry
def send_media_group(chat_id, media: list, caption = ''):
    for i, x in enumerate(media):
        media[i] = {'type': 'photo',
                    'media': x}

    addr = {
        'api': domain % token,
        'chatid': 'sendMediaGroup?chat_id=%s' % chat_id,
        'media': '&media=%s' % json.dumps(media),
        'caption': '&caption=%s' % caption
    }
    return urlopen('{api}{chatid}{media}{caption}'.format(**addr))

@retry
def send_photo(chat_id, photo, caption = '', reply = ''):
    addr = {
        'api': domain % token,
        'method': 'sendPhoto?',
        'channel': 'chat_id=%s' % chat_id,
        'type': '&photo=%s' % photo,
        'caption': '&caption=%s' % caption,
        'reply': '&reply_markup=%s' % reply            
    }    
    return urlopen(
        '{api}{method}{channel}{type}{caption}{reply}'.format(**addr)
    )
@retry
def send_video(chat_id, video, caption = '', reply = ''):
    addr = {
        'api': domain % token,
        'method': 'sendVideo?',
        'channel': 'chat_id=%s' % chat_id,
        'type': '&video=%s' % video,
        'caption': '&caption=%s' % caption,
        'reply': '&reply_markup=%s' % reply            
    }
    return urlopen(
        '{api}{method}{channel}{type}{caption}{reply}'.format(**addr)
    )    

@retry
def send_document(chat_id, document, caption = '', reply = ''):
    addr = {
        'api': domain % token,
        'method': 'sendVideo?',
        'channel': 'chat_id=%s' % chat_id,
        'document': '&document=%s' % document,
        'caption': '&caption=%s' % caption,
        'reply': '&reply_markup=%s' % reply            
    }
    return urlopen(
        '{api}{method}{channel}{document}{caption}{reply}'.format(**addr)
    )    

@retry
def delete_message(chatid, messageid):
    addr = {
        'api': domain % token,
        'method': 'deleteMessage?',
        'chatid': 'chat_id=%s' % chatid,
        'msgid': '&message_id=%s' % messageid,        
    }
    return urlopen('{api}{method}{chatid}{msgid}'.format(**addr))    

@retry    
def addr_callback(callback, text = '', alert = False,
                    url = '', cache_time = 15):
    addr = {
        'api': domain % token,
        'chatid': 'addrCallbackQuery?callback_query_id=%s'
        % callback['id'],
        'text': '&text=%s' % quote(text),
        'alert': '&show_alert=%s' % alert,
        'url': '&url=%s' % url,
        'cache': '&cache_time=%s' % cache_time,         
    }
    
    return urlopen('{api}{chatid}{text}{alert}{url}{cache}'.format(**addr))

@retry        
def get_updates(offset):
    return urlopen(
        domain % token + 'getUpdates?offset=%s' % offset
    ).read().decode('utf-8')

@retry
def get_me():
    return urlopen(domain % token + 'getMe').read().decode('utf-8')

if __name__ == '__main__':
    print(get_me())