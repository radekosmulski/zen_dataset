class Dataset():
    def __init__(self, items, reader, labeler):
        self.items, self.reader, self.labeler = items, reader, labeler

    def __len__(self):
        return len(self.items)

    def __getitem__(self, idx):
        item = self.items[idx]
        return self.reader(item), self.labeler(item)
