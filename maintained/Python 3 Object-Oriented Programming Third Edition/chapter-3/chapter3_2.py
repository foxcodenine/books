class BaseClass:
    num_base_calls = 0 
    
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0 

    def call_me(self):
        super().call_me()
        print("Calling method on Left Subclass")
        self.num_left_calls += 1


class RightSubClass(BaseClass):
    num_right_calls = 0 

    def call_me(self):
        super().call_me()
        print("Calling method on Left Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubClass):
    num_sub_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        self.num_sub_calls += 1

s =Subclass()
s.call_me()
print(s.num_sub_calls, s.num_left_calls, s.num_right_calls,
s.num_base_calls
)

print('\n\n')


#_______________________________________________________________________


class Contact:
    all_contacts = []

    def __init__(self, name="", email="", **kwargs):
        super().__init__(**kwargs)
        self.name = name 
        self.email = email 
        self.all_contacts.append(self)


class AddressHolder:
    
    def __init__(self, street="", city="", state="", code="", **kwargs):
        super().__init__(**kwargs) 
        self.street = street 
        self.city = city 
        self.state = state
        self.code = code


class Friend(Contact):

    def __init__(self, phone="", **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

# by passing the **kwargs parameter we've we can add additional
# parameters that it isn't included included 


# trying classes Contact, AddressHolder & Friend
c = Contact(name='Chris Farrugia', email='foxcodenine@gamil.com')

a = AddressHolder(city='Qormi', street='no name')
a.house='Sweet Caroline'
a.name='Ann Mercieca'
a.email='ann@dontknow.com'

f = Friend(name='Franceska', phone=12121212, email='orangephobia@fts.com')
f.color='Yellow'

print('\n',c.__dict__)
print('\n',a.__dict__)
print('\n',f.__dict__)