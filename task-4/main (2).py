n=int(input("enter n \n"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("this is palindrome number")
else:
 print("this is not a palindrome number")