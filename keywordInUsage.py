''' This shows an example of keyword 'in' used in python 
    The main thing to understand it here is, 
    it's not like the total word should be same like the searching one, 
    if another word just has it, it also works, see below examples
    
    not in usage as well'''

x = "srisurya is a stylish guy"

if("stylish" in x):
    print("Selecting total word here")

if("Stylish" in x):
    print("It is case sensitive so it display's empty due else statement")
else:
    print()

if("sty" in x):
    print("It also consider part's of the words of the sentence")

if("sty " in x):
    print("Don't know how this works, but yeah lets see")
else:
    print("I guess this would be executed")

if("sty " not in x):
    print("sty space anedi ledh kadha mari sentence lo, idhe execute aithadi")
else:
    print("I guess this would be executed")