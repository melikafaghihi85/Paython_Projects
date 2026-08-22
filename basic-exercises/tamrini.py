class Book() :
    book_type = 'horror'
    def __init__(self , page , name ):
        self.page = page 
        self.name = name
    def open(self):
        print(f'opened the {self.name} book which has ({self.page}) pages')

class Darsi(Book):
    def __init__(self,reshte, paye,page,name):
        Book.__init__(self , page , name )
        print('a new darsi book')
        self.reshte = reshte
        self.paye = paye
    def open(self):
         print(f'opened {self.name} of {self.reshte} paye {self.paye} last page {self.page}')
d1 = Darsi('riyazi' , 12 , 400 , '400 nokte')
d1.open()

class Runner():
    def __init__(self,name):
        self.name = name
    def action(self):
        print(f'{self.name} is runing!')
sara = Runner('sara')
sara.action()