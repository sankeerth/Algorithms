class QuickSort(object):
    def __init__(self, array):
        self.array = array
        self.length = len(array)
        self.sort(0, self.length-1)
        assert self.is_sorted()

    def is_sorted(self):
        for i in range(1, self.length):
            if self.array[i] < self.array[i-1]:
                return False
        return True

    def swap(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def sort(self, lo, hi):
        if lo >= hi:
            return
        index = self.partition(lo, hi)
        self.sort(lo, index-1)
        self.sort(index+1, hi)

    def partition(self, lo, hi):
        pivot = self.array[lo]
        i, j = lo+1, hi

        while True:
            while self.array[i] <= pivot and i < hi:
                i += 1

            while self.array[j] >= pivot and j > lo:
                j -= 1

            if i >= j:
                break

            self.swap(i, j)

        self.swap(lo, j)

        return j


quick_sort = QuickSort([10, 12, 9, 6, 3, 7, 8])
print(quick_sort.array)

quick_sort = QuickSort([1, 0, 1, 0, 0, 0, 1])
print(quick_sort.array)

quick_sort = QuickSort([1, 1, 1, 1, 1])
print(quick_sort.array)

quick_sort = QuickSort([1, 1, 1, 1, 0])
print(quick_sort.array)
