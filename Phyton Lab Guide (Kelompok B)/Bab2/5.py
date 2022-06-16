class Dog(): 
"""A simple attempt to simulate a dog"""
def __init__ (self,name,age): 
    """Initialize the name and age attributes."""    
    self.name = name 
    self.age = age 
def sit(self):    
    """Simulate a dog sitting when ordered."""  
    print(self.name.title()+"is now sitting")
def roll_over(self):    
    """Simulate a dog rolling over when ordered."""    
    print(self.name.title()+"rolled over!") 
dog = Dog ("Husky",2)  
dog.sit()  
dog.roll_over()  
  
  
    