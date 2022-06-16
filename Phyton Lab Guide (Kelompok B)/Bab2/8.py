class JustCounter:
    __secretCount = 0 # Private variable.
    publicCount = 0 # Public variable.
    def count(self):
        self.__secretCount += 1 
        self.publicCount += 1
        print(self.__secretCount) 
counter = JustCounter() 
counter.count()
counter.count()
print(counter.publicCount) 
print(counter.__secretCount) # An error is reported,
#indicating that the instance cannot access private variables.


