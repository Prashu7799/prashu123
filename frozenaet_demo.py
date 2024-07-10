x1=({"app1","app2","app3","app4","bye"})
print(type(x1))
# list convert into frozenset
l1=[1,2,3,3,4,4]
X2=frozenset(l1)
x3=x1.union(x2)
print("after adding:::",x3)
for i in x3:
    print(i)