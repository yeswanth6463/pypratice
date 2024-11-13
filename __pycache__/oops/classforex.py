class student:
    inst="pyspiders"
    location="bsavanagudi"
    def __init__(self,name,age,gender,degree,mno,):
        self.name=name
        self.age=age
        self.gender=gender
        self.degree=degree
        self.mno=mno
    def details(self):
        print(f"inst {self.inst}")
        print(f"location {self.location}")
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"gender: {self.gender}")
        print(f"degree: {self.degree}")
        print(f"mobileno: {self.mno}")

st1=student("yeswanth",21,"male","b.tech",9597470128)
st2=student(str(input("enter a name ")),
            int(input("enter a age ")),
            str(input("enter a gender ")),
            str(input("enter a degree ")),
            int(input("enter a mobileno "))
            )
st1.details()
st2.details()