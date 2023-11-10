str=input("enter the string")
count=0
for i in str.lower():
    if(i=='a' or i=='e' or i=='o' or i=='i'or i=='u'):
        count=count+1
print(count)