b="n"
while b=="n":
    n1= float(input("number 1: "))
    s= input("syntax + - / * % ^: ")
    n2= float(input("number 2: "))
    if s == "+":
        a=n1+n2
    elif s=="-":
        a=n1-n2
    elif s=="/":
        a=n1/n2
    elif s=="*":
        a=n1*n2
    elif s=="%":
        a=n1%n2
    elif s=="^":
        a=n1**n2
    else:
        print ("error with syntax")
        continue

    print (n1,s,n2,"=",a)
    b= input("continue with calculation y/n or end: ")
    if b=="end":
        break
    while b=="y":
        n1=a
        s= input("syntax + - / * % ^: ")
        n2= float(input("number 2: "))
        if s == "+":
            a=n1+n2
        elif s=="-":
            a=n1-n2
        elif s=="/":
            a=n1/n2
        elif s=="*":
            a=n1*n2
        elif s=="%":
            a=n1%n2
        elif s=="^":
            a=n1**n2
        else:
            print ("error with syntax")
            continue
        print (n1,s,n2,"=",a)
        b= input("continue y/n or end: ")
    if b=="n":
        continue
    elif b=="end":
        break
    else:
            print("invalid entry, please restart")
            break
