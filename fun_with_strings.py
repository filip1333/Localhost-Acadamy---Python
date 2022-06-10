# generate function generateHuman() which will create an object with the following structure but with random values:
# {name, surname, email:(w oparciu o name i surname), age:(przedział 18-85), phoneNr:random 9 numbers ,country:oneOf([PL,UK,USA])}
# fstring

'''
Filip: I do in console 'pip install names'
'''

import names
import random

countryChoice = ['PL', 'UK', 'USA']

class generateHuman:

    def __init__(self, **kwargs):
        self.firstname = kwargs.get('Name:', names.get_first_name())
        self.surname = kwargs.get('Surname:', names.get_last_name())
        self.email = kwargs.get('Email:', self.firstname.lower() + '.' + self.surname.lower() + '@gmail.com')
        self.age = kwargs.get('Age:', random.randrange(18, 85, 1))
        self.phone = kwargs.get('Phone:', random.choice(range(111111111, 10000000000)))
        self.country = kwargs.get('Country:', random.choice(countryChoice))

    def __str__(self):
        return f"""
        Human:
            Name: {self.firstname}
            Surname: {self.surname}
            Email: {self.email}
            Age: {self.age}
            Phone: {self.phone}
            Country: {self.country}
    """

    def __repr__(self):
        return f'human(firstname="{self._firstname}", ' \
                f'surname={self._surname}, ' \
                f'email={self._email}, ' \
                f'age={self._age}, ' \
                f'phone={self._phone}, ' \
                f'country={self._country})'


generateHuman()

'''
import random
import names
def generate_human():
    human = {}
    print(type(human))
    for i in range(10):
        name = names.get_first_name()   
        human['name'] = name
        surname = names.get_last_name()
        human['surname'] = surname
        human['email'] = name.lower() + '.' + surname.lower() + '@gmail.com'
        human['age'] = random.randrange(18, 85, 1)
        human['phone'] = random.choice(range(111111111, 1000000000))
        countryChoice = ['PL', 'UK', 'USA']
        human['country'] = random.choice(countryChoice)
    return f'{human}'
generate_human()
'''
