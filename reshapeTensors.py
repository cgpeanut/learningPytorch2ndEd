import torch 

print ("\nCreate a tensor")
tensor = torch.arange(9)
print("Original Tensor:")
print(tensor)
# Reshape the tensor
reshaped_tensor = tensor.view(3, 3)
print("\nReshaped Tensor:")
print(reshaped_tensor)

print ("Slicing the tensor")
sliced_tensor = reshaped_tensor[0:2, 0:2]
print("\nSliced Tensor:")
print(sliced_tensor)

print ("Create two tensors")
tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])
print(tensor1)
print(tensor2)
print ("Concatenate the tensors along dimension 0")
concatenated_tensor = torch.cat((tensor1, tensor2))
print("\nConcatenated Tensor:") 
print(concatenated_tensor)

print ("Create two 2D tensors (matrices)")
matrix1 = torch.tensor([[1, 2], [3, 4]])
matrix2 = torch.tensor([[5, 6], [7, 8]])
print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

print ("\nMatrix multiplication using torch.matmul()")
result = torch.matmul(matrix1, matrix2) 
print("\nMatrix Multiplication Result using torch.matmul():")
print(result)

print ("\nMatrix multiplication using @ operator")
result = matrix1 @ matrix2
print("\nMatrix Multiplication Result using @ operator:")
print(result)
