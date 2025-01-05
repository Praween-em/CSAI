import torch
from torch.utils.data import Dataset

class MelDataset(Dataset):
    def __init__(self, data, vocab_size=128):
        self.data = data
        self.vocab_size = vocab_size

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = self.data[idx]
        # Convert text to character indices (ASCII modulo vocab_size)
        text = torch.tensor([ord(c) % self.vocab_size for c in sample["text"]], dtype=torch.long)
        mel = sample["mel"]
        return text, mel
