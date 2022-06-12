def hello(greeting='hello',name='world'): # Default parameters. 
     print('%s, %s!' % (greeting, name)) # Format the output.
hello() # hello，world Default parameter
hello('Greetings') # Greetings，world Position parameter.
hello ('Greetings', 'universe') # Greetings, universe Position parameter.
hello (name= 'Gumby') # hello, Gumby Keyword parameter.

