import os
import torch
import numpy as np

# Paths
mel_dir = r"C:\CSAI MODEL\training_data"  # Directory containing .npy files
output_file = r"C:\CSAI MODEL\processed_dataset.pt"  # Output file for processed dataset

# Initialize dataset list
data = []

# Process each file
for file_name in os.listdir(mel_dir):
    if file_name.endswith(".npy"):
        # Extract text from file name (remove .npy and replace underscores with spaces)
        text = os.path.splitext(file_name)[0].replace("_", " ")
        mel_path = os.path.join(mel_dir, file_name)
        
        # Load Mel spectrogram
        mel = torch.tensor(np.load(mel_path), dtype=torch.float32)
        
        # Append to dataset
        data.append({"text": text, "mel": mel})

# Save processed dataset
torch.save(data, output_file)
print(f"Processed dataset saved to {output_file}")
