#Create a new string by replicating the substring 
# a minimum number of times so that the resulting
#  string is longer than the input string

a = input()
b = int(input())
c = int(input())
x = len(a)
s = a[b:c+1]
dif = len(s)
mul = x//dif
print(s*(mul+1))