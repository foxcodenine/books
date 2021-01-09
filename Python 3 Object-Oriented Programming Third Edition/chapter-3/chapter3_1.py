# Basic inheritance

class Contact:
    all_contacts = [] 

    def __init__(self, name, email):
        self.name = name 
        self.email = email 
        Contact.all_contacts.append(self)

# The all_contacts list is shared by all inctances of the class because 
# it is part of the class definition.

class Supplier(Contact): 
    def order(self, order):
        return(
            "If this were a real system we would send"
            f" {order!r} order to {self.name!r}"
        ) 
# Trying above classes
c = Contact("Some Body", "somebody@example.net")
s = Supplier("Sup Plier", "supplier@example.net")
print(c.name, c.email, s.name, s.email) 
print(s.all_contacts) 
print(s.order("I need coffee"))

# print('\n\n')
#_______________________________________________________________________

# Extending built-insjhf

# extended list
class ContactList(list):
    def search(self, name): 
        """Return all contacts that contain the search value
        in their name."""
        
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts 
     

class Contacts: 
    all_contacts = ContactList() 

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contacts.all_contacts.append(self)

# Trying the above code: 
c1 = Contacts("John A", 'johna@example.net')
c2 = Contacts("John B", 'johnb@example.net')
c3 = Contacts("Jenna C", 'jennac@example.com')
print(Contacts.all_contacts.search('John'))
print([c.name for c in Contacts.all_contacts.search('John')])
print('\n\n')

# extended dict
class LongNameDict(dict):
    def longest_key(self):
        """ a function that return the longest key in the 
        inctanse(that is a dict)"""
        longest = None 
        for key in self:
            if not longest or len(key) > len(longest): 
                longest = key 
        return longest

# Testing class LongName(dict)
longkeys = LongNameDict() 
longkeys['hello'] = 1 
longkeys['longest yet'] = 5 
longkeys['hello2'] = 'world' 
print(longkeys.longest_key())
print('\n\n')

#_______________________________________________________________________

# Overriding and super

class Friend(Contacts):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

# Trying class Friend(Contacts)
J = Friend('James Magri', 'james.magri@gmail.com', 79797979)
print(Contacts.all_contacts.search('James'))
print([J.name, J.email, J.phone])
print('\n\n')

#_______________________________________________________________________

#Multiple inheritance

class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)
        # Add e-mail logic here


class EmailableContact(Contacts, MailSender):
    pass 

# Try classes MailSender and EmaiableContact:

e = EmailableContact("John Smith", "johnsmith@writeme.com") 
print(Contacts.all_contacts)
e.send_mail("Hello there! testing my e-mail here!")
    
#_______________________________________________________________________
