
print("Dame un numero")
num1=input('Numero1: ')
res=0
x=1
while x<=10:
    res=int(num1)*int(x)
    print("{} * {} = {}".format(num1,x,res))
    x=x+1