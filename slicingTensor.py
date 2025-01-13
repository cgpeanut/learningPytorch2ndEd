import pandas as pd
import torch

fish_tensor = torch.tensor(fish_data.iloc[:, :-1].values, dtype=torch.float32) 

# Slicing the first 5 rows and the first 3 columns
sliced_tensor = fish_tensor[:5, :3]

print(f"Sliced Tensor (First 5 rows, First 3 columns):\n{sliced_tensor}")