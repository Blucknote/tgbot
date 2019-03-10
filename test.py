import tgapi

#assert tgapi.set_webhook()
f=tgapi.delete_webhook()
assert f['ok'] == True, "Webhook fail, %s" % f

f=tgapi.send_message(106989752, 'test')
assert f['ok'] == True, "sending message fail, %s" % f

#assert tgapi.send_media_group(106989752,'test')['ok'] == True, "Webhook fail"

img = open('test.jpg', 'rb')
f=tgapi.send_photo(106989752, img.read(), 'test')
assert f['ok'] == True, "sending image fail, %s" % f
img.close()

vid = open('test.mp4', 'rb')
f=tgapi.send_photo(106989752, vid.read(), 'test')
assert f['ok'] == True, "sending video fail, %s" % f
vid.close()


doc = open('test.pdf', 'rb')
f=tgapi.send_document(106989752, doc.read(), 'test')
assert f['ok'] == True, "sending document fail, %s" % f
doc.close()

#assert tgapi.delete_message()

#assert tgapi.addr_callback()

f=tgapi.get_updates(0)
assert f['ok'] == True, "retrieve updates fail, %s" % f

f=tgapi.get_me()
assert f['ok'] == True, "get bot info fail, %s" % f
