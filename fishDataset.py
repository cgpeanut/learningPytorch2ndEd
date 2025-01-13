import pandas as pd
import torch 

#Load the dataset from the URL
url = "https://raw.githubusercontent.com/kittenpub/database-repository/main/Fish_Dataset_Pytorch.csv"
fish_data = pd.read_csv(url)

# Preview the first few rows of the dataset
print(fish_data.head())

# Convert the dataset to a tensor, excluding the label column (assuming the last column is the label)

fish_tensor = torch.tensor(fish_data.iloc[:, :-1].values,dtype=torch.float32)

# Show the shape of the tensor
print(f"Shape of the fish tensor: {fish_tensor.shape}")

# Reshaping the tensor

reshaped_tensor = fish_tensor.view(-1, 2)  # Reshape into 2 columns with inferred rows

print(f"Reshaped Tensor (2 columns): {reshaped_tensor.shape}")

reshaped_tensor_batch = fish_tensor.view(10, -1)  # Reshape into 10 rows with inferred columns

print(f"Reshaped Tensor (10 rows): {reshaped_tensor_batch.shape}")