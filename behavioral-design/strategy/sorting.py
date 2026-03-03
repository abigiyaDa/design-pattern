# The Strategy Interface
from abc import ABC, abstractmethod

from typing import List


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List):
        pass

# Concrete Strategies
class BubbleSortStrategy(Strategy):
    def do_algorithm(self, data: List):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data
    
class QuickSortStrategy(Strategy):
    def do_algorithm(self, data: List):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.do_algorithm(left) + middle + self.do_algorithm(right)
    
# a decorator strategy
class ReverseStrategy(Strategy):
    def __init__(self, base_strategy: Strategy):
        self._base_strategy = base_strategy

    def do_algorithm(self, data: List):
        result = self._base_strategy.do_algorithm(data)
        return list(reversed(result))
    
    
# Context
class Sorter:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def sort(self, data: List):
        return self._strategy.do_algorithm(data)
    
# Example usage
if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    
    sorter = Sorter(BubbleSortStrategy())
    print("Bubble Sort:", sorter.sort(data.copy()))
    
    sorter.set_strategy(QuickSortStrategy())
    print("Quick Sort:", sorter.sort(data.copy()))

    sorter.set_strategy(ReverseStrategy(QuickSortStrategy()))
    print("Reversed Sort:", sorter.sort(data.copy()))