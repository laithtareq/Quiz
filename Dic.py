X = {'Fname':'Laith','Lname':'Tareq','Age':25}
#print(X['Fname'])
#print(type(X))

X['Fname'] = 'Ahmad'
print(X)
#print(X.values())
#print(X.keys())

#print(dir(X))
print(X['Fname'])
#print(X['Location'])  # Error
print(X.get('Location','New'))  # Not Exist