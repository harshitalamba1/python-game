#Calculator
n=int(input("enter the number 1"))
n2=int(input("enter the number 2"))
op=input("enter the operator")
if op=='+':
    print("the answer is",n+n2)
elif op=='-':
    print("the answer is",n-n2)
elif op=='*':
    print("the answer is",n/n2)
elif op=='/':
    print("the answer is",n/n2)
elif op=='%':
    print("the answer is",n%n2)
else:
    print("invalid operator")