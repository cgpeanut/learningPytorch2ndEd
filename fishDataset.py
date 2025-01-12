import pandas as pd
import torch 
import numpy as np

a = np.array([
    np.array([0.5, 1.0, 2.0], dtype=np.float16),
    np.array([4.0, 6.0, 8.0], dtype=np.float16),
])

b = torch.from_numpy(a)

print(a.dtype) # This should not be 'object'
print(b)

# Load the dataset from the URL
url = "https://raw.githubusercontent.com/kittenpub/database-repository/main/Fish_Dataset_Pytorch.csv"
fish_data = pd.read_csv(url)

# Preview the first few rows of the dataset
print(fish_data.head())

# Convert the dataset to a tensor, excluding the label column (assuming the last column is the label

fish_tensor = torch.tensor(fish_data.iloc[:, :-1].values, dtype=torch.float32)

# Show the shape of the tensor
print(f"Shape of the fish tensor: {fish_tensor.shape}")
