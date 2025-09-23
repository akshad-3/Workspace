class employe:
    language="python" #this is an class atrribute
    salary=120000
    
    def getinfo(self):
        print(f"the language used if {language},& salary is {salary}")

mike=employe()
mike.name="Mike" #this is an instance atrribute
print(mike.name,mike.language,mike.salary)