#Create a 3x3 matrix with values ranging from 0 to 8.
import numpy as np
np.arange(9).reshape(3,3)

#Create a random array of size 10 and sort it
x=np.random.random(10)
np.sort(x)

#Remove from one array those items that exist in another For example, a1 = [1, 2, 3], a2 = [1, 3] --> result = [2]
a1=np.array([1, 2, 3])
a2=np.array([1,3])
np.setdiff1d(a1,a2)

#Get the positions where elements of two arrays match For example, a1 = [1, 2, 3, 10], a2 = [5, 4, 3, 10] --> result = [2, 3]
a1=np.array([1,2,3,10])
a2=np.array([5,4,3,10])
np.intersect1d(a1,a2)

#Replace "Michael" with "Mike" in x x = np.array(['Hello name is Michael'], dtype=np.str)
x = np.array(['Hello name is Michael'], dtype=np.str)
x[0].replace("Michael","Mike")

#Lex x be an array [[ 1, 2],[ 3, 4]] Rotate x 90 degrees counter-clockwise. expected result = [[3, 1], [4, 2]]
x=np.array([[1,2],
         [3,4]])
np.rot90(x,-1)
