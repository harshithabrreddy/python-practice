#lenght of the name check more than  5 characteristics
name=input('Enter  Your Name:')
print("Lenght of Name:",len(name))
res="More than 5 characters" if(len(name)>5)else "not more than 5 characteristics"
print(res)