# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# import array as arr

a = [1,2,3,4,5,6]
'''print(a[:])
'''
b = []
for i in a[::-1]:
    b.append(i)
print(b)

string = "hello, my name is Peter, I am 26 years old"
print(string.split())

def multi(n):
    return n*n
    
num = [1,2,3,4,5]
result = map(multi,num)
print(list(result))

x = lambda a: a+2
print(x(4))

f = lambda gt,yt:gt*yt
print(f(3,4))

num1 = [1,2,3]
x = map(lambda x:x+1,num1)
print(list(x))
