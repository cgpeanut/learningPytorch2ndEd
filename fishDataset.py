import pandas as pd
import torch 

# Load the dataset from the URL
url = "https://raw.githubusercontent.com/kittenpub/database-repository/main/Fish_Dataset_Pytorch.csv"
fish_data = pd.read_csv(url)

# Preview the first few rows of the dataset
print(fish_data.head())

# Convert the dataset to a tensor, excluding the label column (assuming the last column is the label

#fish_tensor = torch.tensor(fish_data.iloc[:, :-1].values,dtype=torch.float32)
fish_tensor = torch.tensor(fish_data.iloc[:, :-1].values, dtype=torch.float32)

# Show the shape of the tensor
print(f"Shape of the fish tensor: {fish_tensor.shape}")