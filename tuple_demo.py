# creating Tuple obj
t=("hello",10,True,False,15.0)
print(t," datatype:::",type(t))

# tuple convert into list type
l1=list(t)
l1[0]="bye"
print("after manuplating :::",l1)
#Iterating objs
for x in t:
    print(x)

t3=("prashanth","satish","ankith")
(x,y,z)=t3
print("x value::",x)
print("y value::",y)
print("z value::",z)

t4=("kvrao","svrao","pvrao","nvrao","dvrao","gvrao")
(n1,n2,*n3)=t4
print("n1 value::",n1)
print("n2 value::",n2)
print("n3 value::",n3)

t5=("svreddy","avreddy","jagan","kuika","pvreddy")
(s1,*s2,s3)=t5
print("s1 objs:::",s1)
print("s2 objs:::",s2)
print("s3 objs:::",s3)

t6=("anji","babu","pavan","nani","mikki","suma")
l3=list(t6)
r1=l3[0:2]
r2=l3[2:4]
r3=l3[4:]
print(l3[0:2])
print(l3[2:4])
print(l3[4:])