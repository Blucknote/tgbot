import tgapi

#assert tgapi.set_webhook()
f=tgapi.delete_webhook()
assert f['result'] == True, "Webhook fail, %s" % f.json()

f=tgapi.send_message(106989752, 'test')
assert f['result'] == True, "sending message fail, %s" % f.json()

#assert tgapi.send_media_group(106989752,'test')['result'] == True, "Webhook fail"

img = open('test.jpg', 'rb')
f=tgapi.send_photo(106989752, img.read(), 'test')
assert f['result'] == True, "sending image fail, %s" % f.json()
img.close()

vid = open('test.mp4', 'rb')
f=tgapi.send_photo(106989752, vid.read(), 'test')
assert f['result'] == True, "sending video fail, %s" % f.json()
vid.close()


doc = open('test.pdf', 'rb')
f=tgapi.send_document(106989752, doc.read(), 'test')
assert f['result'] == True, "sending document fail, %s" % f.json()
doc.close()

#assert tgapi.delete_message()

#assert tgapi.addr_callback()

f=tgapi.get_updates(0)
assert f['result'] == True, "retrieve updates fail, %s" % f.json()

f=tgapi.get_me()
assert f['result'] == True, "get bot info fail, %s" % f.json()
