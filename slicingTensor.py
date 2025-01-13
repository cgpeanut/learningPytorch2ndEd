import pandas as pd
import torch

 # Load the dataset from the URL
url = "https://raw.githubusercontent.com/kittenpub/database-repository/main/Fish_Dataset_Pytorch.csv"
fish_data = pd.read_csv(url)

# Preview the first few rows of the dataset
print(fish_data.head())

fish_tensor = torch.tensor(fish_data.iloc[:, :-1].values, dtype=torch.float32) 

# Slicing the first 5 rows and the first 3 columns
sliced_tensor = fish_tensor[:5, :3]

print(f"Sliced Tensor (First 5 rows, First 3 columns):\n{sliced_tensor}")