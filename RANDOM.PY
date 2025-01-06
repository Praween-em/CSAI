import torch

data = torch.load(r"C:\CSAI MODEL\processed_dataset.pt")
print(type(data))
print(data[:1])  # Print the first two elements to inspect the structure
