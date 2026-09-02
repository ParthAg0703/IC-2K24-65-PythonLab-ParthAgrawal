star = "*"
count = 5
print(star * ((count * 2)-1))
for i in range(1,count):
    num = (i * 2) -1
    print(("*" * (count - i) + " " * num + "*" * (count - i)))
for i in range(count-1,0,-1):
    num = (i * 2) -1
    print(("*" * (count - i) + " " * num + "*" * (count - i)))
print(star * ((count * 2)-1))