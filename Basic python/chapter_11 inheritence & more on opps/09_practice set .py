#1----->create a class c2-d vector and use it to crack another class represent a 3d  vector
'''class c2dvec:
    def __init__(self, i, j ):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
class c3dvec(c2dvec):
    def __init__(self, i, j, k ):
        super().__init__(i, j)
        self.kcap = k
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k "

v2d = c2dvec(1,3)        
v3d = c3dvec(1,9,7)

print(v2d)
print(v3d)'''
#2---> create a class pets from a class animals and further create class dog from pets add a method bark to class dog
'''class animals:
      animalType="Mammal"

class pets:
      color = "white"

class dog:
    @staticmethod  
    def bark(): 
         print("Bow bow...")     

d = dog()         
d.bark()'''

#3----> create a class employee add salary and increment properties in it write a method salary after increment method with a @property decoretor with a setter which change the value of increment based on the salary 
# salaryafterincrement = salary * increment
'''class employee:
    salary = 2000
    increment =1.5
    @property
    def salaryafterincrement(self): 
        return self.salary*self.increment 
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,sai): 
        increment = sai/self.salary

e =employee()
print(e.salaryafterincrement)

print(e.increment)
e.salaryafterincrement= 5000
print(e.salaryafterincrement)
print(e.increment)'''

#4---> write a class vector represent a vector of n dimenssion overload the + and * operator which calculates the sum and the  dot product of them..
'''class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i
    def __add__(self,c):
        return Complex(self.real + c.real, self.imaginary+ c.imaginary)
    def __mul__(self,c):
        mulReal = (self.real * c.real- self.imaginary * c.imaginary)
        mulimaginary = (self.real * c.imaginary+ self.imaginary * c.real)
        return Complex (mulReal, mulimaginary)
     
    def __str__(self):
      if self.imaginary < 0 :
            return f"{self.real}-{self.imaginary}"
            return f"{self.real} + {self.imaginary}i"
c1 =Complex(3,2)        
c2= Complex(1,7)
print(c1*c2)
print(c1+c2)'''

#5-----> write a class vector representing a vector  of n dimentions , overload the + and  * operator which calculates the sum and dot product of the.
'''class vector:
    def __init__(self,vec):
        self.vec = vec 
    def __str__(self):
        str1 = " "   
        index =  0 
        for i in  self.vec:
            str1+= f"{i}a{index}+"
            index+=1
        return str1[:-1]    
    def __add__(self,vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i]+ vec2.vec[i])
        return vector(newList)
    def __mul__(self,vec2):
        sum=0
        for i in range (len(self.vec)):
            sum += self.vec[i]+ vec2.vec[i]  
            return sum
        

v1 = vector([1,4,55,77,88])
v2 = vector([1,4,87,88,78])
print(v1+v2)
print(v1*v2)'''

#6--->write __ sh__ () method to print vector as follows: 7i + 8j +10k
'''class vector:
    def __init__(self,vec):
        self.vec = vec 
    def __str__(self):
       return f"{self.vec[0]}i+{self.vec[1]}j+{self.vec[2]}k"   
v1 = vector([1,4,6])

print(v1)  '''

#7----> overwrite  the __len__() method on vector of problem 5 to display the dimentions of the 
class vector:
    def __init__(self,vec):
        self.vec = vec 
    def __str__(self):
        str1 = " "   
        index =  0 
        for i in  self.vec:
            str1+= f"{i}a{index}+"
            index+=1
        return str1[:-1]    
    def __add__(self,vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i]+ vec2.vec[i])
        return vector(newList)
    def __mul__(self,vec2):
        sum=0
        for i in range (len(self.vec)):
            sum += self.vec[i]+ vec2.vec[i]  
            return sum
    def __len__(self):
        return len(self.vec)    

v1 = vector([1,4,55,77,88])
v2 = vector([1,4,87,88,78])
print(v1+v2)
print(v1*v2)
print(len(v1))
print(len(v2))
