a=13
c=0
while(1):
    n=int(input("enter the number: "))
    if(n<a):
        print("the number is greater")
        c=c+1
    elif(n>a):
        print("the number is samller")
        c=c+1
    else:
        print("correct guess")
        c=c+1
        break
print(f"You took {c} attempts")
