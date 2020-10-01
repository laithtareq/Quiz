def Sum(X,Y):
    Z = []
    for i in range(len(X)):
        Z.append(X[i]+Y[i])
    return Z

List1 = [1,4,5,7,8]
List2 = [7,2,4,2,10]
print(Sum(List1,List2))


def Sum_Map(x,y):
    return x+y
Z = list(map(Sum_Map,List1,List2))
print(Z)