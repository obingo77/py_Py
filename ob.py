class ob:
  def __init__(self, name, age):
    self.name = name
    self.age = age 
  def func(self):
    print("hello" + self.age)
    print(self.name)

print(ob.__doc__)
p1 = ob("obrien", 45)
p1.func()
    




  