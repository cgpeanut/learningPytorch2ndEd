import torch

print ("Creating an Empty Tensor:")
empty_tensor = torch.empty(3, 2)
print(empty_tensor)

print ("Creating a Tensor Filled with Zeros:")
zero_tensor = torch.zeros(3, 2)
print(zero_tensor)

print ("Creating a Tensor Filled with Ones:")
ones_tensor = torch.ones(3, 2)
print(ones_tensor)

print ("Creating a Random Tensor")
random_tensor = torch.rand(3, 2)
print(random_tensor)

print ("Create tensor with default data type (float32)")
tensor = torch.ones(3, 2)
print(tensor) 
print("Data Type: ", tensor.dtype)

print ("Changing tensor data type to float64")
tensor = tensor.to(torch.float64) 
print("\nAfter Changing Data Type to float64:") 
print(tensor) 
print("Data Type: ", tensor.dtype) 

print ("Changing tensor data type to int32")
tensor = tensor.to(torch.int32) 
print("\nAfter Changing Data Type to int32:") 
print(tensor) 
print("Data Type: ", tensor.dtype)

print ("Changing tensor data type to boolean")
tensor = tensor.to(torch.bool) 
print("\nAfter Changing Data Type to boolean:")
print(tensor)
print("Data Type: ", tensor.dtype)

print ("Create two tensors")
tensor1 = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
tensor2 = torch.tensor([5, 6, 7, 8], dtype=torch.float32)
print("Tensor 1:", tensor1)
print("Tensor 2:", tensor2)

print ("\nAddition")
result = tensor1 + tensor2 
print("\nAddition Result: ", result)

print ("\nSubtraction")
result = tensor1 - tensor2 
print("\nSubtraction Result: ", result)

print ("\nMultiplication")
# Multiplication (Element-wise)
result = tensor1 * tensor2 
print("Multiplication Result: ", result)

print ("\nDivision")
# Division
result = tensor1 / tensor2
print("Division Result: ", result)
