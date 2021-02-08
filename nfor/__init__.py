import itertools
from multiprocessing import Pool

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

class NForPool(nfor):
    def __init__(self, variables, function, n_cpu=4):
        super().__init__(variables)
        self.function = function
        self.pool = Pool(processes=n_cpu)

    def __call__(self):
        ress = []
        for job in self:
            res = self.pool.apply_async(self.function, args=job)
            ress.append(res)
        for res in ress:
            res.get()