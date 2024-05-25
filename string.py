def string():
    cap,sma,dig,vow=0,0,0,0
    num=input("enter any string : ")
    for i in num:
        if i>="A" and i<="Z":
            cap=cap+1
        elif i>="a" and i<="z":
            sma=sma+1
        elif i.isdigit()==True:
            dig=dig+1
        else:
            pass
    for i in num:
        if i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='e' :
            vow=vow+1 
    print("capital letter is {} and smaller letter is {} and vowel is {} and digit is {}".format(cap,sma,vow,dig))
string()
