import tgapi

#assert tgapi.set_webhook()
f=tgapi.delete_webhook()
assert f['error_code'] == 200, "Webhook fail"

f=tgapi.send_message(106989752, 'test')
assert f['error_code'] == 200, "sending message fail"

#assert tgapi.send_media_group(106989752,'test')['error_code'] == 200, "Webhook fail"

img = open('test.jpg', 'rb')
f=tgapi.send_photo(106989752, img.read(), 'test')
assert f['error_code'] == 200, "sending image fail"
img.close()

vid = open('test.mp4', 'rb')
f=tgapi.send_photo(106989752, vid.read(), 'test')
assert f['error_code'] == 200, "sending video fail"
vid.close()


doc = open('test.pdf', 'rb')
f=tgapi.send_document(106989752, doc.read(), 'test')
assert f['error_code'] == 200, "sending document fail"
doc.close()

#assert tgapi.delete_message()

#assert tgapi.addr_callback()

f=tgapi.get_updates(0)
assert f['error_code'] == 200, "retrieve updates fail"

f=tgapi.get_me()
assert f['error_code'] == 200, "get bot info fail"
