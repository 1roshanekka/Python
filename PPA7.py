n = input()
sum=0
for i in range(len(n)):
    sum = sum + int(n[i])
print(sum)

sum = 0.0
n = int(n)
while(n//10>0):
    a = n%10
    n = n//10
    sum = sum + a
#when its single digit then it doesn't go inside the loop
print(int(sum+n))
