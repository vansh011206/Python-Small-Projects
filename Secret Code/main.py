import random

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def coding(word):
    if len(word)>=3:
        f1 = random.choice(alpha)
        f2 = random.choice(alpha)
        f3 = random.choice(alpha)
        f4 = random.choice(alpha)
        f5 = random.choice(alpha)
        f6 = random.choice(alpha)
        newword = f1 + f2 + f3 + word[1:] + word[0] + f4 + f5 + f6
        print(f'The New Coded word is : {newword}')
        return
    elif len(word)==2:
        new = word[1] + word[0]
        print(new)
        return
    else :
        print(word)
        return

def decoding(word):
    if len(word)>=3:
        approxword = word[3:(len(word)-3)]
        newword = approxword[-1] + approxword[:-1]
        print(f'The New Decoded Word is : {newword}')
        return
    elif len(word)==2:
        new = word[1] + word[0]
        print(new)
        return
    else:
        print(word)
        return
    

user_input = input('Enter a Word:\n')    
operation = input('What You want to do Code or decode ?\n').lower()
try:
    if operation == 'code':
        coding(user_input)
    elif operation == 'decode':
        decoding(user_input)
    else:
        print('Invalid!')
            
except Exception as e:
    print(e)
               
               