class A: 
    def __init__(self, a): 
        self.a = a 
    def __lt__(self, other): 
        if(self.a<other.a): 
            return "ob1 kurang dari ob2"
        else: 
            return "ob2 kurang dari ob1"
    def __eq__(self, other): 
        if(self.a == other.a): 
            return "Keduanya Sama"
        else: 
            return "Tidak Sama"
                  
ob1 = A(2) 
ob2 = A(3) 
print(ob1 < ob2) 
  
ob3 = A(4) 
ob4 = A(4) 
print(ob1 == ob2)
