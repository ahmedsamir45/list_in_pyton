word=input("enter a word : ")
pal=""
for i in range(len(word)-1,-1,-1):
    pal+=word[i]
print(pal)
list_word=[]
for i in range(len(word)):
    list_word.append(word[i])
list_word.reverse()
print(list_word)
