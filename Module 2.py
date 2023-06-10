n = int(input("Which number would you like to investigate (0 to exit):"))
for i in range (1,11):
    print(n,"*",i,"=",n*i)
    if n == 0:
        print("Thank you for using the calculator!")
        break
    
