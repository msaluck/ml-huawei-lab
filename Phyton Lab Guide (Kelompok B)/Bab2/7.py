class Parent: # Define the parent class.
    parentAttr = 100
    def __init__(self):
        print("Invoke the parent class to construct a function.") 
    def parentMethod(self):
        print('Invoke a parent class method.')
    def setAttr(self, attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print("Parent attribute:", Parent.parentAttr)
class Child(Parent):  # Define a child class.
    def __init__(self): 
        print("Invoke a child class to construct a method.") 
    def childMethod(self): 
        print('Invoke a child method.')
c = Child() # Instantiate a child class.
c.childMethod() # Invoke the method of a child class.
c.parentMethod() # Invoke the method of a parent class.
c.setAttr(200) # Invoke the method of the parent class again to set the attribute value.
c.getAttr() # Invoke the method of the parent class again to obtain the attribute value. 



