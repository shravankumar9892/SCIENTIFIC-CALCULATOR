#######SCIENTIFIC CALCULATORS########
####defining functions over here###
def raisedtosame(x):
    if x>0:
        x=x**x
        print('answer is',x)
    else:
        print('Invalid input')
def squares(x):
    x=x*x
    print('answer is:',x)
    return x
def sum_cubes(x):
    x=x*x*(x+1)*(x+1)/4
    print('in sum_cubes(x):z=',x)
    return x
def sum_squares(n):
    n=n*(n+1)*(2*n+1)/6
    print('for sum of cubes:S(n)=',n)
    return n
def sum_linear(n):
    n=n*(n+1)/2
    print('for sum of natural numbers:S(n)=',n)
    return(n)
def sin(x):
    """let user input value of x in degrees and not in radians"""
    pi=3.14
    x=x*pi/180
    x=x-(x**3/6)+(x**5/120)-(x**7/5040)+(x**9/362880)-(x**11/39916800)
def cos(x):
    """value of angle only in degrees"""
    pi=3.14
    x=x*pi/180
    x=1-(x**2/2)+(x**4/24)-(x**6/(24*30))+(x**8/(24*30*56))-(x**10/(24*30*56*90))
option=str(input('press a for algebric calculator and t for trigonometric calculator:\n'))
if option=='a':
  print('1]Press (1)for addition')
  print('2]Press(2)for subtraction')    
  print('3]Press(3)for multiplication')
  print('4]Press(4)for division')
  print('5]Press(5)for sum of cubes')
  print('6]Press(6)for sum of squares')
  print('7]Press(7)for sum of natural numbers')
  print('8]Press(8)for cube root of any number')
  print('9]Press(9)for square root of any number')
  print('1o]Press(10)for square of any number')  
  print('11]Press(11)for a number raised to itself')
  x=int(input('Please enter your choice:\n'))
  if x==1:
        print('enter the values of a and b')
        a=int(input('what is a?'))
        b=int(input('what is b?'))
        sum=a+b
        print(sum)
  if x==3:
        print('enter the values of a and b')
        a=int(input('what is a?'))
        b=int(input('what is b?'))
        multiply=a*b
        print(multiply)
  if x==2:
        print('enter the values of a and b')
        a=int(input('what is a?'))
        b=int(input('what is b?'))
        sub=a-b
        print(sub)
  if x==4:
        print('enter the values of a and b')
        a=int(input('what is a?'))
        b=int(input('what is b?'))
        div=a/b
        print(div)
  if x==5:
      y=int(input('Enter the value of y:\n'))
      sum_cubes(y)
  if x==6:
      y=int(input('Enter the value of y:\n'))
      sum_squares(y)
  if x==7:
       y=int(input('Enter the value of y:\n'))
       sum_linear(y)
  if x==8:
      n=int(input("enter the value of n:\n"))
      x=0
      if n>0:
        while x**3<n:
          x=x+0.01
        print(x)    
      if n<0:
          s=-1*n
          while x**3<s:
           x=x+0.01
          print(-1*x)
  if x==9:
      n=int(input("enter the value of n:\n"))
      x=0
      while x**2<n:
          x=x+0.01
      print(x)    
  if x==10:
      sq=float(input('Enter the value of any number:'))
      squares(sq)
      print(squares(sq))
  if x==11:
      rise=float(input('Enter value of the number for which you choose this operation:'))
      raisedtosame(rise)
if option=='t':
   print("Press 1a] for sine function")
   print("Press 2a]for cosine function") 
   z=str(input('Please enter your choice:\n'))
   if z=='1a':
       alpha=float(input('Enter the value of angle in degrees only,please'))
       sin(alpha)
       print(sin(alpha))
   if z=='2a':
       beta=float(input('Enter the value of angle in degrees only,please:'))
       cos(beta)
       print(cos(beta))
print(" ")        
print('THANKS A LOT!!!')      

