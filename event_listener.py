import json
import time

import yaml
from . import tgapi

lastmsg = 0
message_handlers = []
callbacks_handlers = []


def handle(recieved, handlers=message_handlers):
    if len(recieved) > 1:
        if not isinstance(recieved, dict):      #we got few messages at once
            messages = [msg['message'] for msg in recieved]  #throwing useless
        else:
            messages = [recieved]
    else:
        messages = None
    for handler in handlers:
        if messages is not None:     #this also means we have multiple messages
            done = [*map(handler, messages)]
            return done
        else:           #thats why if not we transfer single msg directly
            if 'message' in recieved[0]:
                handler(recieved[0]['message'])
            elif 'callback_query' in recieved[0]:
                handler(recieved[0]['callback_query'])


def dispatcher(updates, webhook=False, cooldown=1):
    global lastmsg
    if updates is not None:

        commands = [
            *filter(
                lambda x:'message' in x and 'text' in x['message'],
                filter(
                    lambda y: y['update_id'] > lastmsg, updates['result']
                ) if not webhook else [updates]
            )            
        ]

        key_check = (
            updates['callback_query'] if 'callback_query' in updates
            else None
        )

        callbacks = [
            *filter(lambda x: 'callback_query' in x, updates['result'])            
        ] if not webhook else key_check

        if commands:
            handle(commands)
        elif callbacks:
            handle(callbacks, callbacks_handlers)        

    else:
        commands = [{'update_id': 0}]
        callbacks = [{'update_id': 0}]

    if not webhook:
        time.sleep(cooldown)
        lastmsg = max(
            map(
                lambda x: x.get('update_id', 0),
                commands if commands else callbacks
            ),
            default=lastmsg            
        )        


def start_server(port=9696):
    from http.server import HTTPServer, BaseHTTPRequestHandler 

    class handler(BaseHTTPRequestHandler):
        def _set_headers(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

        def do_GET(self):
            self._set_headers()
            self.wfile.write('get response')

        def do_HEAD(self):
            self._set_headers()

        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            dispatcher(post_data, True)
            self._set_headers()

    server_address = ('', port)
    httpd = HTTPServer(server_address, handler)
    httpd.serve_forever()


def polling():
    tgapi.delete_webhook()
    while True:
        dispatcher(tgapi.get_updates(lastmsg + 1))    


def start(conffile='conf.yml'):
    tgapi.conf = yaml.load(open(conffile,'r').read())
    if 'webhook' in tgapi.conf.keys():
        if tgapi.conf['webhook']:
            response = tgapi.set_webhook(
                '%s%s' %
                (tgapi.conf['domain'], tgapi.conf['token']), tgapi.conf['ssl']
             )
            print(response.read().decode('utf-8'))
            start_server(
                tgapi.conf['port'] if 'port' in tgapi.conf.keys() else 9696
            )
        else:
            polling()
    else:
        polling()
