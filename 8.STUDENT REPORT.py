#student report
name=str(input("name : "))
sno=int(input("sno;"))
tel=int(input("tel : "))
hin=int(input("hin : "))
eng=int(input("eng : "))
tot=tel+hin+eng
avg=tot/3
print(name)
print(sno)
print("marks in tel ,hin , eng=",tel,hin,eng)
print(tot)
print(avg)
if(tel<35 or hin<35 or eng<35):
    print("fail")
else:
    if(avg>75):
        print("distinsion")
    elif("avg>=65"):
        print("1st class")
    elif(avg>=55):
        print("2nd class")
    elif(avg>=45):
        print("pass")
    else:
        print("fail")