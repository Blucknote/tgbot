import tgapi

#assert tgapi.set_webhook()

assert tgapi.delete_webhook()['error_code'] == 200, "Webhook fail"

assert tgapi.send_message(106989752, 'test')['error_code'] == 200, "sending message fail"

#assert tgapi.send_media_group(106989752,'test')['error_code'] == 200, "Webhook fail"

img = open('test.jpg', 'rb').read()
assert tgapi.send_photo(106989752, img, 'test')['error_code'] == 200, "sending image fail"
img.close()

vid = open('test.mp4', 'rb').read()
assert tgapi.send_photo(106989752, vid, 'test')['error_code'] == 200, "sending video fail"
vid.close()

doc = open('test.pdf', 'rb').read()
assert tgapi.send_document(106989752, doc, 'test')['error_code'] == 200, "sending document fail"
doc.close()

#assert tgapi.delete_message()

#assert tgapi.addr_callback()

assert tgapi.get_updates(0)['error_code'] == 200, "retrieve updates fail"

assert tgapi.get_me()['error_code'] == 200, "get bot info fail"