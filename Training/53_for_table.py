import time
i=0
t=[]
a=1
b=10
tt=[]

for i in range(101):
    tt.append(i)
    if i==0:
        t.append(i)
        continue
    elif i>=a and i<b:
        t.append(i)
    elif i%10==0:
     t.append(i)
     print(t)
     # time.sleep(5)
     t.clear()
     a+=10
     b+=10
     continue
    else:
        pass

# print(tt)