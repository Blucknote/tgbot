import re

def on_message(text):
    def wrapper(fn):
        def inner(message):
            if re.findall(text, message['text']):
                return(fn(message))
        return inner
    return wrapper


def on_callback(data):
    def wrapper(fn):
        def inner(callback):
            if re.findall(data, callback['data']):
                return(fn(callback))
        return inner
    return wrapper


def on_media(message):
    raise NotImplementedError("Not implemented")
  
def on_document(document):
    raise NotImplementedError("Not implemented")

def on_sticker(document):
    raise NotImplementedError("Not implemented")
