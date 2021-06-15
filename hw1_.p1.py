#digit sum 4
num=int(input (" input a 4-digit number: ")) 
a=num//1000 
b=(num%1000)//100
c=(num%100)//10
d=num%10
print(a+b+c+d)