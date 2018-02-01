import json

class Keyboard:
    def __init__(
        self, inline: bool, rows = 2, resize_keyboard = False,
        one_time_keyboard = False, selective = False        
    ):
        self.inline = inline
        self.rows = rows
        
        self._keyboard = []
        for row in range(self.rows + 1):
            self._keyboard.append([])
            
        self.kb = {
            'inline_keyboard' if self.inline else 'keyboard': self._keyboard,
        }
        
        if not inline:
            self.kb.update(locals())
            
            #clearing
            self.kb.pop('inline')
            self.kb.pop('row')
            self.kb.pop('rows')
            self.kb.pop('self')
        
    def __len__(self):
        return len(self._keyboard)
    
    def __getitem__(self, item):
        return self._keyboard[item]
        
    def __str__(self):
        return '%s' % json.dumps(self.kb)
            
    def add_button(
        self, row, caption, link = '', callback = '',
        req_contact = False, req_location = False
    ):
        self._keyboard[row].append(
            dict(
                text = caption,
                url = link,
                callback_data = callback
                ) if self.inline else dict(
                    text = caption,
                    request_contact = req_contact,
                    request_location = req_location
                )
            )