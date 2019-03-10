from urllib.request import quote
import json
import yaml
import fire
import requests

domain = 'https://api.telegram.org/bot%s/'

conf = yaml.load(open('conf.yml', 'r').read())


def set_webhook(self_domain_path: str, certificate):
    addr = {
        'api': domain % conf['token'],
        'method': 'setWebhook?',
        'url': 'url=%s' % self_domain_path,
        'cert': '&certificate=%s' % open(certificate, 'r'),
    }

    return requests.get('{api}{method}{url}{cert}'.format(**addr)).json()


def delete_webhook():
    return requests.get('%sdeleteWebhook' % (domain % conf['token'])).json()


def send_message(chatid, msg, reply_markup=''):
    addr = {
        'api': domain % conf['token'],
        'chatid': 'sendMessage?chat_id=%s' % chatid,
        'text': '&text=%s' % quote(msg),
        'reply': '&reply_markup=%s' % reply_markup
    }

    return requests.get('{api}{chatid}{text}{reply}'.format(**addr)).json()


def send_media_group(chat_id, media: list, caption=''):
    for i, x in enumerate(media):
        media[i] = {'type': 'photo',
                    'media': x}

    addr = {
        'api': domain % conf['token'],
        'chatid': 'sendMediaGroup?chat_id=%s' % chat_id,
        'media': '&media=%s' % json.dumps(media),
        'caption': '&caption=%s' % caption
    }

    return requests.get('{api}{chatid}{media}{caption}'.format(**addr)).json()


def send_photo(chat_id, photo, caption='', reply=''):
    addr = {
        'api': domain % conf['token'],
        'method': 'sendPhoto?',
        'channel': 'chat_id=%s' % chat_id,
        'type': '&photo=%s' % photo,
        'caption': '&caption=%s' % caption,
        'reply': '&reply_markup=%s' % reply
    }

    if isinstance(photo, bytes):
        requests.post(
            '{api}{method}{channel}'.format(**addr), files={'photo': photo}
        ).json()
    else:
        return requests.get(
            '{api}{method}{channel}{type}{caption}{reply}'.format(**addr)
        ).json()


def send_video(chat_id, video, caption='', reply=''):
    addr = {
        'api': domain % conf['token'],
        'method': 'sendVideo?',
        'channel': 'chat_id=%s' % chat_id,
        'type': '&video=%s' % video,
        'caption': '&caption=%s' % caption,
        'reply': '&reply_markup=%s' % reply
    }

    if isinstance(video, bytes):
        requests.post(
            '{api}{method}{channel}'.format(**addr), files={'video': video}
        ).json()
    else:
        return requests.get(
            '{api}{method}{channel}{type}{caption}{reply}'.format(**addr)
            ).json()


def send_document(chat_id, document, caption='', reply=''):
    addr = {
        'api': domain % conf['token'],
        'method': 'sendDocument?',
        'channel': 'chat_id=%s' % chat_id,
        'document': '&document=%s' % document,
        'caption': '&caption=%s' % caption,
        'reply': '&reply_markup=%s' % reply
    }

    if isinstance(document, bytes):
        requests.post(
            '{api}{method}{channel}'.format(**addr), files={'docunent': document}
        ).json()
    else:
        return requests.get(
            '{api}{method}{channel}{document}{caption}{reply}'.format(**addr)
        ).json()


def delete_message(chatid, messageid):
    addr = {
        'api': domain % conf['token'],
        'method': 'deleteMessage?',
        'chatid': 'chat_id=%s' % chatid,
        'msgid': '&message_id=%s' % messageid,
    }

    return requests.get('{api}{method}{chatid}{msgid}'.format(**addr)).json()


def addr_callback(callback, text='', alert=False, url='', cache_time=15):
    addr = {
        'api': domain % conf['token'],
        'chatid': 'addrCallbackQuery?callback_query_id=%s'
        % callback['id'],
        'text': '&text=%s' % quote(text),
        'alert': '&show_alert=%s' % alert,
        'url': '&url=%s' % url,
        'cache': '&cache_time=%s' % cache_time,         
    }

    return requests.get('{api}{chatid}{text}{alert}{url}{cache}'.format(**addr)).json()


def get_updates(offset):
    return requests.get(
        domain % conf['token'] + 'getUpdates?offset=%s' % offset
    ).json()


def get_me():
    return requests.get(domain % conf['token'] + 'getMe').json()


if __name__ == '__main__':
    print(get_me())
    #fire.Fire()
