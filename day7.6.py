#lenth of the word
size=int(input('Enter the size of the list:'))
WorldList=[]
for i in range(size):
    val=input('Enter  the word:')
    WordList.append(val)
print("User Entered List is:",WorldList)
Len=list(map(lambda w:len(w),WordList))
print("Length of the Words in the list:",Len)