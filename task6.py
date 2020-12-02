#adding +2

li=[1,2,3,4,5]
for i in li:
    print(i,i+2)


#pattern
def pattern(n):    
  for i in range(n,0,-1):
     for j in range(i,0,-1):
       print(j,end=" ")
     print("\r")
  
n=5
pattern(n)

#fibonacci sequence

def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b
 
# Driver Program
 
print(fibonacci(9))


#armstrong number

def isArmstrong(x): 
      
    n = order(x) 
    temp = x 
    sum1 = 0
      
    while (temp != 0): 
        r = temp % 10
        sum1 = sum1 + power(r, n) 
        temp = temp // 10
  
    # If condition satisfies 
    return sum1 
  
# Driver code 
x = 153

if(isArmstrong(x)==153):
  print(isArmstrong(x)) 
  























