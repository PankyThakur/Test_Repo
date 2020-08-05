capitals={'a':1,'b':2,'c':3,'d':4,'e':5}
print(capitals)
a=input('Enter the element to be deleted')
if a in capitals:
    del capitals[a]
print(capitals)