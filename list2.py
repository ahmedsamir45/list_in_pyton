codzila = ['programming','python','tutotrial','html','css']
tutorial = ['extend','list','codzila','r']

t=tutorial.count('r')
print(t)
#codzila+=tutorial
#codzila = codzila + tutorila
codzila.extend(tutorial)
print(codzila)


codzila.append([True,False,3,'t'])
print(codzila)

codzila.insert(0,'r')
print(codzila)



codzila.remove('list')
print(codzila)


codzila.pop()
#non parmetar
print(codzila)

what_is_poped = codzila.pop()
print('what_is_poped ',what_is_poped)





codzila.clear()
#non parmetar
print(codzila)


y = [5,36,234,9,2,1,7]
x=y.copy()
y.sort()
print(y)
print(x)


























