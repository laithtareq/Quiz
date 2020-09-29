def Vectorial(Num):
    Ans = 1  # Start Value

    for i in range(1,Num+1):  # i = [0......Num+1] 
        Ans*=i  # Multibly avrery itration
        
    return Ans

print(Vectorial(5))  # print(5!) >>> print(120)

def Sumation(Num):
    Ans = 0  # Start Value

    for i in range(1,Num+1):  # i = [0......Num+1] 
        Ans+=i  # Multibly avrery itration
    
    return Ans

print(Sumation(5))  # print(5!) >>> print(120)