#exceptions handling
# When there are no errors -> NOTHING TO HANDLE 
print("Program Execution Started")

num1=10
num2=5

print(num1/num2)

print("program excuetion completed")


print("="*25)


#when there are errors ->
print("program excuetion started")

num1=10
num2=0

#print(num1/num2) #ZeroDivisionError: division by zero

print("program exceution completed")

print('='*25)

#when there are errors ->how to handle by yourself

print("program excecution started")

num1=10
num2 =0
 
try:
   print(num1/num2) # ZeroDivisionError: division by zero
except:
   print("OOPS! You cannot divide number by zero - it's a MATH rule")
   print("Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")

print("Program Execution Completed")

print("=" * 50)


#when there are mutliple errors
print("program excuetion started")

data=[1,5,'python',0.5]
#data=[1,2,5]
#TypeError: unsupported operand type(s) for /: 'int' and 'str'
# ZeroDivisionError: division by zero
# in future one more issue

for num in data:
   try:
      print(1/num)
   except:
      print("OOPS some problem occured")


print("program excuetion completed")

print('='*25)

# When there are multiple errors -> Need To Present Specific Error
print("Program Execution Started")
data = [1,2,'python',0,5]

# TypeError: unsupported operand type(s) for /: 'int' and 'str'
# ZeroDivisionError: division by zero
# in future one more issue

for num in data:
    try:
        print(1/num)
    except TypeError:
        print("OOPS! Don't pass string, we cannot divide a string with number")
    except ZeroDivisionError: # this is not correct way
        print("OOPS! You cannot divide number by zero - it's a MATH rule")
        print("Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")
        
print("Program Execution Completed")

print("=" * 50)


# When there are errors -> without else
print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print(num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! You cannot divide number by zero - it's a MATH rule")
    print("Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")

print("Calculation Successful")
print("Program Execution Completed")

print("=" * 50)

# When there are errors -> without else
print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print(num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! You cannot divide number by zero - it's a MATH rule")
    print("Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")

print("Calculation Successful")
print("Program Execution Completed")

print("=" * 50)



# When there are errors -> without else
print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print(num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! You cannot divide number by zero - it's a MATH rule")
    print("Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")

print("Calculation Successful")
print("Program Execution Completed")

print("=" * 50)


# When there are errors -> without else
print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print(num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! You cannot divide number by zero - it's a MATH rule")
    print("Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")

print("Calculation Successful")
print("Program Execution Completed")

print("=" * 50)

#when there are errors ->with else ,finally
print("Program Execution Started")

num1 = 10
num2 = 0

try:
    print(num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! You cannot divide number by zero - it's a MATH rule")
    print("Check More Info - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Successful")
finally:
    print("program excuetion completed -closing all connections")

print("="*50)
   
# User Defined Exception 
# InvalidAgeException
# InvalidEmailException
class InvalidScoreError(Exception):
    pass 

try:
    score = int(input("Enter Score 0-100 "))
    if score < 0 or score > 100:
        raise InvalidScoreError("Score Must be between (0-100)")
    print("Your Score Is Valid")
except InvalidScoreError as e :
    print("Error: ",e)