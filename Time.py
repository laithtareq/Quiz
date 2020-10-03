import timeit
X = [1,2,4,5,7,9]
Y = [4,2,7,8,6,9]
Sum_Map = lambda x,y:x+y
Z = map(Sum_Map,X,Y)
print(Z)
Z = list(map(Sum_Map,X,Y))
print(Z)
Setup1 = """
X = [1,2,4,5,7,9]
Y = [4,2,7,8,6,9]
Z = []
for i in range(len(X)):
    Z.append(X[i]+Y[i]) 
    """
Setup2 = """
X = [1,2,4,5,7,9]
Y = [4,2,7,8,6,9]
Sum_Map = lambda x,y:x+y
map(Sum_Map,X,Y)
 """
Time1 = timeit.timeit(Setup1,number=10000)
Time2 = timeit.timeit(Setup2,number=10000)
#print(round(Time1,5))
#print(round(Time2,5))
#print(Time1/Time2)