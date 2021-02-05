import itertools

class nfor(object):
    def __init__(self, variables):
        self.combinations = list(itertools.product(*variables))
        self.len = len(self.combinations)
        self.counter = 0

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < self.len:
            combination = self.combinations[self.counter]
            self.counter += 1
        else:
            raise StopIteration
        return combination

    def __len__(self):
        return self.len

    def __getitem__(self, idx):
        return self.combinations[idx]