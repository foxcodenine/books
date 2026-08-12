# We'll be modeling a Document class that might be used in a
# text editor or word processor.

class Document: 
    def __init__(self):
        self.characters = [] 
        self.cursor = Cursor(self) 
        self.filename = '' 

    def insert(self, character, bold=False, italic=False, underline=False):
        # I updated this function from the book 
        # so you can select better the bold, italic & underline options.
        b=bold 
        i=italic 
        u=underline
        if not hasattr(character, 'character'):
            character = Character(character, bold=b, italic=i, underline=u) 
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward() 
        
    def delete(self): 
        # I have found two mistake here in the book:

        # you need adjust the position of the cursor 
        # by -1 to select the last character.
        del self.characters[self.cursor.position - 1]  
        # and after you delete the character move 
        # the cursor back 1 space.
        self.cursor.position -= 1 

    def save(self): 
        with open(self.filename, 'w') as f: 
            f.write(''.join(self.characters)) 
    
    @property 
    def string(self): 
        return "".join(str(c) for c in self.characters)

#_______________________________________________________________________ 

class Cursor: 
    def __init__(self, document):
        self.document = document 
        self.position = 0 
    
    def forward(self): 
        self.position += 1 

    def back(self): 
        self.position -= 1 
    
    def home(self):
        while self.document.characters[self.position - 1].character != "\n": 
            self.position -= 1 
            if self.position == 0: 
                # Got to beginning of file before newline 
                break 

    def end(self): 
        while (
            self.position < len(self.document.characters) 
            and self.document.character[self.position].character != "\n"
        ):
            self.position += 1
#_______________________________________________________________________ 

class Character: 
    def __init__(
        self, character, bold=False, italic=False, underline=False
    ):
        assert len(character) == 1 
        self.character = character
        self.bold = bold 
        self.italic = italic 
        self.underline = underline 

    def __str__(self):
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else '' 
        
        return bold + italic + underline + self.character

#_______________________________________________________________________ 


    

