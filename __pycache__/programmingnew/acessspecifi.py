class A:
    def pubs(self):
        print("public acess specifier")
    def _prot(self):
        print("protected acess specifier")
    def __prv(self):
        print("private acess specifier")

obj=A()
obj.pubs()
obj._prot()
obj.__prv()












