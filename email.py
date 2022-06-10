# Create class that creates an email with fields
# - FROM
# - TO
# - CC
# - BCC
# - TITLE
# - HTML
# Methods:
# save to jsonO
# loads from json
import json

class Email:

    def __init__(self, from_who, to, cc, bcc, title, html):
        self.from_who = from_who    
        self.to = to
        self.cc = cc    
        self.bcc = bcc
        self.title = title
        self.html = html

    def __str__(self):
        return f'''
            From: {self.from_who}
            To: {self.to}
            CC: {self.cc}
            BCC: {self.bcc}
            Title: {self.title}
            HTML: {self.html}
    '''

    def __repr__(self):
        return f'Mail From = {self.from_who}, Mail To = {self.to}'

    def to_dict(self):
        mail_dict = {'From:':self.from_who, 'To:':self.to, 'CC:':self.cc, 'BCC:':self.bcc, 'Title:':self.title, 'HTML:':self.html}
        return mail_dict

    def save_to_json(self):
        with open('test.json', 'w', encoding="utf-8") as outfile:
            json.dump(self.to_dict(), outfile)

    def load_from_json(self):
        with open('test2.json', 'r') as openfile:
            return Email(**json.load(openfile))


em1 = Email('ania@g.c', 'filip@g.c', 'localhost@g.c', 'mother@g.c, father@g.c', 'Other test', '<p>hi!</p>')
em1.save_to_json()
print(Email.load_from_json('test2.json'))
