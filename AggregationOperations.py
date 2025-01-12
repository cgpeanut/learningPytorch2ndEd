import torch

print ("Create a tensor")
tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)

print("Tensor:")
print(tensor)

print ("Sum of tensor") 
sum_val = torch.sum(tensor) 
print("\nSum of Tensor Elements: ", sum_val)

print ("Mean of tensor") 
mean_val = torch.mean(tensor) 
print("\nMean of Tensor Elements: ", mean_val)

print ("Max of tensor")
max_val = torch.max(tensor) 
print("\nMax of Tensor Elements: ", max_val)

print ("Min of tensor") 
min_val = torch.min(tensor) 
print("\nMin of Tensor Elements: ", min_val)