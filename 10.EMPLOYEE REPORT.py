#EMPLOYEE REPORT 
name=input("employee name : ")
empid=int(input("employee id : "))
bs=int(input("basic salary : "))
hra=float(input("hra : "))
da=float(input("da : "))
ta=float(input("ta : "))
pf=float(input("pf : "))
tot= bs+((bs*hra)/100)+((bs*ta)/100)+((bs*da)/100)
gsal=tot-((bs*pf)/100)
print(name)
print(empid)
print(bs)
print(tot)
print(gsal)
if(bs<=20000):
    print("worker")
elif(bs<=35000):
    print("superwiser")
elif(bs<=45000):
    print("manager")
elif(bs<=70000):
    print("bosss")
else:
    print("chairmen")