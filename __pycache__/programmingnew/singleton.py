class singleton:
    __ab=10
    def __init__(self):
        if singleton.__ab==10:
             singleton.__ab=self
             
        else:
            raise Exception("it is single time object")

o1=singleton()
o2=singleton()
            
        