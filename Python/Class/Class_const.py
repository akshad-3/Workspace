class employe:
    lang="python"
    salary=1200000
    
    def __init__(self,name,lang,salary):
        self.name=name
        self.lang=lang
        self.salary=salary
        print("hello and welcome Python")

mike=employe("mike","javascript",1300000)
print(mike.name,mike.lang,mike.salary)