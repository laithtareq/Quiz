
Name = 'Laith Tariq'
def myfunction(Name):
    for x in Name[0::4]:
        if x=='H':
            continue
        print(x.upper())
    
myfunction(Name)