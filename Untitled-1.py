a=int( input("donner la 1er note") )
b=int( input("donner la 2eme note") )
c=int( input("donner la 3eme note") )
m=(a+b+c)/3
if m>16:
    print("tres bien")
elif m>14 or m==14:
    print("bien")
elif m>12 or m==12:
    print("assez bien")
elif m>10 or m==10:
    print("passable")
else:
    print("insuffisant")