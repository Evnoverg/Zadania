stroke=input("Введите строку")
a=0
e=0
u=0
i=0
o=0
y=0
for n in stroke:
    letter=n.lower()
    if letter=="a":
     a+=1
    elif letter=="e":
        e+=1
    elif letter=="y":
        y+=1
    elif letter=="u":
        u+=1
    elif letter=="i":
        i+=1
    elif letter=="o":
        o+=1
string='a=%s e=%s y=%s u=%s i=%s o=%s' %(a, e, y, u, i, o)
print(string)