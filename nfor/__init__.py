"""NFor module documentation."""
import itertools
from multiprocessing import Pool

class NFor:
    """``NFor`` - An iterator for nested for loops (high dimensional grids)."""
    def __init__(self, variables):
        """Initialize the ``nfor`` object``.

        :param list variables: A list of arrays/lists, where every combination
            of every element is desired in the high dimensional grid.
        """
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

class NForPool(NFor):
    """```NForPool`` object - to run nested for loops on ``multiprocessing``."""
    def __init__(self, variables, function, n_cpu=4):
        """Initialize the ``NForPool`` object.

        :param list variables: List of variables to pass to ``NFor``.
        :param func function: Function to run on every combination.
        :param int n_cpu: Number of CPUs to use in the process pool.
        """
        super().__init__(variables)
        self.function = function
        self.pool = Pool(processes=n_cpu)

    def __call__(self):
        ress = []
        results = []
        for job in self:
            res = self.pool.apply_async(self.function, args=job)
            ress.append(res)
        for res in ress:
            result = res.get()
            results.append(result)
        return results