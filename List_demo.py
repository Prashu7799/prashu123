# Creating List
x=["app1","app2","app3","app3","app4","app5","app6","app3",10]
#it will display the second index obj and data type
print("2 index::",x[2],"datatype :::",type(x))
# Iterating objs
for i in x:
    print(i)

# update 2 index obj
x[2]="hai"
print(" after updating 2 index::",x[2],"datatype :::",type(x))
# update more than one obj
x[2:4]=["prashanth","satish"]
print(" after updating 2 objs :::",x[2]," 3rd index::"+x[3])
# after 3rd index we want insert new Element
x.insert(3,"hello")
print(x) 
# remove all
x.clear()
print(x)