#operations using function

def fun(c,d):
   f=c+d
   z=c-d
   x=c/d
   y=c*d
   print(f)
   print(z)
   print(x)
   print(y)

a=input("enter a:")
b=input("enter b:")
a=int(a)
b=int(b)
fun(a,b)

#default argument in functions

def covid(a,body_temperature=98):
    print('temperature of ',a,'is',body_temperature) 


patient_name=input("enter the name")

covid(patient_name)
