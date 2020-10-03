
class Operations:
    def __init__(self,**kwargs):
        self.Data = kwargs
        
    def Sum(self):
        return self.Data['X1']+self.Data['X2']
    def Sub(self):
        return self.Data['X1']-self.Data['X2']
    def Mult(self):
        return self.Data['X1']*self.Data['X2']
    def Div(self):
        if self.Data['X2']==0:
            return "Div by Zero"
        else:
            return self.Data['X1']/self.Data['X2']

X = Operations(X1=4,X2=0)

print(X.Sum())
print(X.Sub())
print(X.Div())