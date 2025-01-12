import torch

# Create a tensor and move it to the GPU
x = torch.rand(5, 3)
x = x.cuda()
# Perform a matrix multiplication on the GPU
y = torch.rand(3, 3).cuda()
result = torch.matmul(x, y)
print(result)
print("Tensor is on GPU:", result.is_cuda)
