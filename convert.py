import torch
import numpy as np

# Your test array without 'dtype=object'
a = np.array([
        np.array([0.5, 1.0, 2.0], dtype=np.float16),
        np.array([4.0, 6.0, 8.0], dtype=np.float16),
])

b = torch.from_numpy(a)

print(a.dtype) # This should not be 'object'
print(b)
