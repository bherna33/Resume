class A:
    def __init__(self, r):
        self.name = ""
        self.r = r
    
    def dis(self, n):
        self.name = n
        return self.name
    
    def d(self):
        return self.r
        
a = A(4)
a.name = "branden"
print(a.name)
B = a.dis("test")
C = a.dis("Br")
print(B)
print(C)
print(a.d())

test ={}
test["college"] = {"state": {"degree": "date"}}
print(test)