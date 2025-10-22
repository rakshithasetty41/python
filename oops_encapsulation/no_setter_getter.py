# No Encapsulation & No Setter - Getter

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

obj=student("rakshi",99)
print(obj.name)
print(obj.marks)

obj.marks=100
print(obj.marks)

obj.name="maahi"
print(obj.name)
