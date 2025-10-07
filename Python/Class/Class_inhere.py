class a:
    company="infocys"
    def show(self):
        print(f"This Company is a {self.company}")
        
class b(a):
    employ_id=123445
    employ_name="rahul"
    
    def info(self):
        print(f"{self.employ_name} his ID is {self.employ_id} & he works in {self.company}")
    
A=a()
B=b()
A.show()
B.info()