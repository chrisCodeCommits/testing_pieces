
# This algorithm count the number of vowels inside a dictionairy.


a = {'me':'11', 'you': '22', 'us': '33'}


# this is the step where I extract keys from the dictionairy and convert the result to tuple
def findkeys(mydict):
    for each in mydict:
        return tuple(list(iter(mydict)))
  
  
        
# this function  join strings into one for my next operation         
def join_str(x):
    return ','.join(x)
        
        
        
# this is the function that will count vowels on my string   
def vowelsNumber (x):
    vowels = 0
    for target in x:
        if target in 'aAeEiIoOuU':
            vowels += 1
    return vowels 
    
    
    
# now the final function 
def count_keys_vowels(x):
    return (vowelsNumber(join_str(findkeys(x))))
    
    


print (count_keys_vowels(a))
    