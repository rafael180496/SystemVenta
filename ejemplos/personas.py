
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hello(self):
        print('hola mi nombre es {} y mi edad es {}'.format(self.name,self.age))
        
    
if __name__ == "__main__":
    person=Person('david',34)
    person.say_hello()

    
