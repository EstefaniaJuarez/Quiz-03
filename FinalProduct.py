#Number 1
def dot(vector01,vector02):
  '''
  This function takes in two vectors as its inputs and produces the resulting dot product. The dot product is computed by multiplying corresponding elements of each vector. Once the multiplication is complete, the numbers are then added together, resulting in an integer.
  '''
  n = len(vector01)
  p = len(vector02)
  #The following line is checking that the length of both vectors is equal to ensure that multiplication is possible
  if n==p:
    x=0
    #This for loop is taking each  corresponding element, multiplying them, and adding them together for the final integer.
    for i in range(len(vector01)):
      x += vector01[i]*vector02[i]
    return x 
  else:
    print("invalid input")
    return None

#This is test 1 that passes
vector01=[1,2,3]
vector02=[3,4,5]
print(dot(vector01,vector02))
#This is test 2 that returns invalid input
#vector01_invalid[5,6,7,8]
#vector02_invalid[3,2,1]
#print(dot(vector01_invalid,vector02_invalid))

#Number 2
def vecSubtract(vector03,vector04):
  '''
  The function vecSubtract takes in two vectors and returns the difference of the two. After the difference of each pair of corresponding elements has been computed, it then takes the number and puts it in a new list to return the updated vector.
  '''
  n = len(vector03)
  p = len(vector04)
  if n==p:
    x=[]
    #this for loop subtracts the two elements and then appends the difference into the new vector, x
    for i in range(len(vector03)):
      x.append(vector03[i]-vector04[i])
    return x
  else:
    print("invalid input")
    return None

#This is test 1 that returns invalid input
vector03=[1,2,3,4]
vector04=[3,4,5]
print(vecSubtract(vector03,vector04))
#This is test 2 that returns the difference vector
#vector03_valid=[10,20,30]
#vector04_valid=[5,10,20]
#print(vecSubtract(vector03_valid,vector04_valid))

#Number 3
def scalarVecMulti(scalar1,vector05):
  '''
  This function takes in a scalar and vector as its inputs. The scalar is multiplied to each element of the vector. The result is then placed into the new vector, x.
  '''
  x = []
  #This for loop takes the multiplication of each element of the vector and the scalar and appends the product to new vector x.
  for i in range(len(vector05)):
    x.append(vector05[i]*scalar1)
  return x

#This is test 1 that works
vector05 = [1,2,3]
scalar1 = 3
print(scalarVecMulti(scalar1,vector05))
#This is test 2 that breaks
#vector05_invalid="Texas Tech"
#scalar1=10
#print(scalarVecMulti(scalar1,vector05_invalid))

#Question 4
import math
def infNorm(vector06):
  '''
  This function takes in a vector and produces the norm of the vector using the infinity norm. The infinity norm takes the absolute value of each element in the vector. It results in the maximum element value of the vector, after the absolute value has been taken.
  '''
  x=0
  for i in range(len(vector06)):
    #This line is taking the absolute value of each element in the vector with the condition of it being greater than 0. It then takes the maximum value of the elements and returns it.
    if abs(vector06[i]) > x:
      x= abs(vector06[i])
  return x

#This is test 1 that passes
vector06=[-10,2,3,13]
print(infNorm(vector06))
#This is test 2 that fails
#vector06_invalid=10,20,30
#print(infNorm(vector06_invalid)

#Question 5
def normalize(vector07):
  '''
  This function takes a vector and calculates the normalized vector.The norm of vector has been calculated in question 4 and is being referenced for this question. Then, the normalized vector is calculated by dividing each element in the specified vector by the norm using the infinity norm.  
  '''
  norm = infNorm(vector07)
  x = []
  #This for loop divides each element of vector07 and divides it by the norm of vector07. It then appends the number to the new normalized vector, x.
  for i in range(len(vector07)):
    x.append(vector07[i]/norm)
  return (x)
  
#This is test 1 that passes
vector07=[1,2,3,13]
print(normalize(vector07))

#This is test 2 that fails
#vector07_invalid="Red Raiders"
#print(normalize(vector07_invalid))
