star = "*"
count = 10
print(star * ((count * 2)-1))
for i in range(1,count+1):
    num = (i * 2) -1
    print(("*" * (count - i) + " " * num)*2)