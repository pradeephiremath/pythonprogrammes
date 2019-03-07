def func1():
	print("Hi")
	print("Hello")

func1()


def func2(a):
	print("Hi\n",a)

func2(2)

def func3(a,b,c):
	d=c+a+b
	print(a,b,c,"\n",d)
	return d

func3(1,2,3)


def func4(university="IITB"):
	print("I'm studying in ",university)

func4("IITG")
func4("IITD")
func4()

def func5(x,y):
	z=x+y
	print("Hi",x,y,"\n",z)
	return z
	

#func5(8,9)
	
def func6():
	s=func5(1,3)
	print("Sum is ",s)


func6()