import numpy as np
#Array creation
arr1=np.array([1,2,3])
print(arr1)

#2d array
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)

#zeros array
arr3=np.zeros((2,3))
print(arr3)

ones=np.ones((3,3))
print(ones)

# Range of numbers
arr4 = np.arange(0, 10, 2)  # start=0, stop=10, step=2
print("Range array:", arr4)

print("="*25)


#Indexing->indexing starts at 0
#1 2 3 4 5 6 7 8 9
#0 1 2 3 4 5 6 7 8->index
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr[1])
print(arr[-1])
print(arr[4])

#2d array->indexing        0     1        2


#                     0    1     2       3
                        
#                     1    4     5       6

matrix=np.array([[1,2,3],[4,5,6]])
print(matrix[0,1])
print(matrix[1,2])

print("="*25)
#slicing
arr5=np.array([10,20,30,50,60,40,80,90])
print(arr5[1:])
print(arr5[:-1])
print(arr5[2:6])
print(arr5[::-1])

#nd slicing
mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat[:,0])
print(mat[:2,:])
print(mat[:])
print(mat[::-1])
print(mat[1])

print("="*25)

#mathematical operations
data=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(data)
print(data*2)
print(data+5)
print(data-10)

print(np.sqrt(data))
print(np.power(data,2))
print("="*25)
#Axis wise
#axis=0 is a column,axis=1 is arow
print(np.sum(data,axis=0))
print(np.sum(data,axis=1))

print(np.mean(data,axis=0))
print(np.mean(data,axis=1))

print("="*25)
#statistical operation
print(np.min(data))
print(np.max(data))
print(np.mean(data))
print(np.var(data))
print(np.std(data))
print(np.median(data))
print(np.min(data,axis=0))
print(np.min(data,axis=1))
print(np.max(data,axis=0))
print(np.max(data,axis=1))
print("="*25)
#reshaping

data = np.arange(12)
print("Original Data:", data)
reshaped_data = data.reshape(3, 4)
print("Reshaped Data :", reshaped_data)

print("="*25)
#brodacast
row= np.array([10, 20, 30, 40])
print("Row Vector:", row)
result = reshaped_data + row
print("Result after Broadcasting (each row + row_vector):", result)

col = np.array([[100], [200], [300]])  # shape (3,1)
result2 = reshaped_data + col
print("Result after Broadcasting (each column + col_vector):", result2)
print("="*25)
#save and load operations
data = np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])
print(data)
np.save("my_data.npy", data)
print(" Array saved successfully as 'my_data.npy'")

loaded_data = np.load("my_data.npy")
print("Loaded Array:", loaded_data)

print("="*25)
#Compared NumPy’s performance with standard Python
#using python list
list_data = [1, 2, 3, 4, 5]
list_result = [x + 10 for x in list_data]
print("Python List Result:", list_result)
list=[x*5 for x in list_data]
print("Python List Result:",list)

# Using NumPy array
np_data = np.array([1, 2, 3, 4, 5])
np_result = np_data + 10
print("NumPy Array Result:", np_result)
np_result = np_data * 10
print("NumPy Array Result:", np_result)

