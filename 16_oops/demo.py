#oops basic
data=10
print(type(data))
  
class employee:
    pass

employ_obj=employee()
print(type(employ_obj))


# Student -> Real World Entity
class student:
    
    # attributes / variables 
    student_name="rakshi"
    student_mail="rakshi@gmail.com"
    #statements
    print(student_name)
    print(student_mail)
# function (outside the class)
def fun():
    #variables
    student_name="royal"
    student_mail="royal@gmail.com"
   
    #statements
    print(student_name)
    print(student_mail)
#for function call is must
fun()


#Student -> Real World Entity
class Student:
    # attributes / variables 
    student_name = "mike"
    student_email = "mike@gmail.com"
    
    # method
    def info(self):
        # student_email = "john@gmail.com"
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email) 

student_one_obj = Student()
student_two_obj = Student()
student_three_obj = Student()
# method call is required 
student_one_obj.info() # TypeError: Student.info() takes 0 positional arguments but 1 was given
student_two_obj.info()
student_three_obj.info()

# __init__() -> Constructor
class student:
    #constructor
    def __init__(self,student_name,student_age):
        self.student_name=student_name
        self.student_age=student_age
        
    #methods
    def info(self):
        print("student name:",self.student_name)
        print("student age:",self.student_age)

ravi_obj=student("ravi",80)
subbu_obj=student("subbu",90)
krish_obj=student("mahi",85)
#method call
ravi_obj.info()
subbu_obj.info()
krish_obj.info()

