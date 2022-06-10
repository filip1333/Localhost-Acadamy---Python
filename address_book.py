# Create a data structure related to the address book						
# Class "address book"						
# 	It is to have a list of all contacts, a list of contact groups,				
# 	it is supposed to do Create Read Update Remove, display contact list in an appropriate way, possibility to sort the list by phrases

# Single contact" class						
# 	It is to have Name, surname, email address, date of modification,				
# 	it is to do Create an object, update the modification date, display it in the appropriate format when called				

# Class "Contact group"						
# 	is to have a contact list				
# 	it is to do Create Read Update Remove

from datetime import date

class SingleContact:
    def __init__(self, firstname, lastname, mail):
        self.firstname = firstname
        self.lastname = lastname
        self.mail = mail
        self.modification_date = date.today().strftime(f"%d.%m.%Y")

    def __str__(self):
        return f'Contact first name: {self.firstname}, Contact last name: {self.lastname}, Contact mail: {self.mail}, Last modification date: {self.modification_date}'

    def __repr__(self):
        return f"contact name='{self.firstname}' lastname='{self.lastname}' mail='{self.mail}' last modification date='{self.modification_date}'"

    def contact_to_dict(self):
        dict_one_contact = {'firstname': self.firstname, 'lastname':self.lastname, 'mail':self.mail}
        return dict_one_contact

    def update(self, **kwargs):
        self.modification_date = date.today().strftime(f"%d.%m.%Y")
        for k in kwargs.keys():
            if k in self.contact_to_dict().keys():
                self.__setattr__(k, kwargs[k])            
        return self

class ContactGroup:
    def __init__(self, name):
        self.name = name
        self.contact = []

    def __repr__(self):
        return f"group name='{self.name}'"

    def add_single_contact(self, single_contact):
        self.contact.append(single_contact)

    def display_name(self):
        return f'Group name: {self.name}'

    def display_group_contacts(self):
        return f'Group name: {self.name}: {self.contact}'

    def delete_whole_group(self):
        del self.name

    def update_group_name(self, name, new_name):
        self.name = new_name
        return self.display_name()

    def delete_one_contact(self, one_contact):
        self.contact.remove(one_contact)
        return self.display_group_contacts()

class AddressBook:
    def __init__(self, my_all_contacts, my_all_groups):
        self.my_all_contacts = my_all_contacts
        self.my_all_groups = my_all_groups

    def read_all_contacts_list(self):
        return self.my_all_contacts

    def read_all_groups_list(self):
        return self.my_all_groups

    def add_single_contact(self, new_contact:SingleContact):
        self.my_all_contacts.append(new_contact)

    def sort(self, value):
        if value in ['firstname', 'lastname', 'mail', 'modification_date']:
            return sorted(self.my_all_contacts, key=lambda single_contact:getattr(single_contact, value))
        elif value == 'name':
            return sorted(self.my_all_groups, key=lambda group_name:getattr(group_name, value))
        else:
            return f"This value is invalid, you don't have it"

    def remove_contact(self, exist_contact):    
        self.my_all_contacts.remove(exist_contact)

    def remove_group(self, exist_group):
        self.my_all_groups.remove(exist_group)


mom = SingleContact('Renata', 'Rybka', 'renatarybka@gmail.com')
print(mom)
print(mom.contact_to_dict())
print(mom.update(lastname='Rybcia', mail='l@l'))
print(mom.update(firstname='Renia'))
print(mom)
first_new_contact = SingleContact('Kasia', 'Po.', 'kasiap@gmail.com')
print(first_new_contact)
second_new_contact = SingleContact('Ania', 'Rybka', 'annarybka@gmail.com')
print(second_new_contact)
first_group = ContactGroup('Family')
first_group.add_single_contact(mom)
first_group.add_single_contact(second_new_contact)
print(first_group.display_name())
print(first_group.display_group_contacts())
second_group = ContactGroup('Friends')
second_group.add_single_contact(first_new_contact)
print(second_group.display_name())
print(second_group.display_group_contacts())
first_group.delete_whole_group()
print(first_group.display_name())
first_group.update_group_name('Family', 'Relatives')
print(first_group.display_name())
print(first_group.display_name(), second_group.display_name())
first_group.delete_one_contact(mom)
print(first_group.display_group_contacts())
book = AddressBook([mom, first_new_contact, second_new_contact], [first_group, second_group])
print(book.read_all_contacts_list())
print(book.read_all_groups_list())
book.add_single_contact(new_contact=SingleContact('Klaudia', 'Ge.', 'klaudiag@gmail.com'))
print(book.read_all_contacts_list())
print(book.sort('firstname'))
print(book.sort('lastname'))
print(book.sort('mail'))
print(book.sort('modification_date'))
book.remove_contact(mom)
print(book.read_all_contacts_list())
print(book.sort("lover's"))
print(book.sort('name'))
book.remove_group(second_group)
print(book.read_all_groups_list())
