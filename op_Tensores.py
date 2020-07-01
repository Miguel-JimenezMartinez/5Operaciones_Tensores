import torch 


a=torch.tensor([                   #Declaramos un tensor "a" (hago el llenado para practicar) 
	[1,2,3],
	[4,5,6],
	[7,8,9]], dtype=torch.int)
b=torch.ones(3,3,dtype=torch.int) #Declaro un tensor "b" y lo lleno de unos e indico que son de tipo entero
c=torch.rand(3,3)                 #Declaro un tensor "c" con numeros random
d=torch.rand(3,3)                 #Declaro un tensor "c" con numeros random

s1=torch.add(a,b)                 #Funcion para sumar a y b
s2=c+d                            #Suma de c y d
m1=torch.mul(a,b)                 #Funcion para multiplicar a y b
m2=c*d
co1=torch.cat((a,b))              #Concatenamos tensores que tengan el mismo tipo de dato
co2=torch.cat((c,d))


print("a=",a,"\n\n","b=",b,"\n\n","a+b=",s1) 
print("\nc=",c,"\n\n","d=",d,"\n\n","c+d=",s2) 
print("\na*b=",m1)
print("\nc*d=",m2)
print("\n",co1)
print("\n",co2)                              