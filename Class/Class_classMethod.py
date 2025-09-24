class a:
    a=1
    @classmethod #But if we use @classmethod the instance will not work any more.
    def show(self):
        print(f"the value of class attribute is {self.a}")

b=a()
b.a=45 #if we change the value in instance it will change the value of a LINE->3
b.show()#-->Output still we be 1 coz we used the @classmethod
