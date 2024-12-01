

class person:
   def greet(self):
       print("hello sir")
       self.info()
       print("thanks for using it")

   
   def __init__(self, name, occupation, salary):
    self.name=name
    self.occupation=occupation
    self.salary=salary
    self.greet()

   def info(self):
       print (f"my name is {self.name} and I am a {self.occupation} my curremt income is {self.salary}")


a=person("kamla" ,"teacher",120000)
b=person("rohit" ,"principal",180000)
c=person("vikash" ,"lab a",150000)
a.info()
b.info()
c.info()





