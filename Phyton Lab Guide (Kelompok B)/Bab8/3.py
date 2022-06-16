#Create a generator through a yield keyword.
def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1+num2
        current += 1
        yield num
return 'done'    
g=fib(5)
while True:
    try: 
        x = next(g)
        print("value:%d"%x)
    except StopIteration as e:
    print("Generator return value:%s"%e.value)
    break
















