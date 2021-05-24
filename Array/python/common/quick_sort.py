class QuickSort(object):
    def __init__(self, nums):
        self.nums = nums
        self.length = len(nums)

    def isSorted(self):
        for i in range(1, self.length):
            if self.nums[i] < self.nums[i-1]:
                return False
        return True

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def sort(self):
        self.performSort(0, self.length-1)
        return self.nums

    def performSort(self, lo, hi):
        if lo >= hi:
            return
        pivot = self.partition(lo, hi)
        self.performSort(lo, pivot-1)
        self.performSort(pivot+1, hi)

    def partition(self, lo, hi):
        pivot = lo
        # i, j = lo+1, hi # could use i and j as copies of lo and hi instead
        while True:
            while lo <= hi and self.nums[lo] <= self.nums[pivot]: # i < hi
                lo += 1
            
            while hi >= lo and self.nums[hi] >= self.nums[pivot]: # j > lo
                hi -= 1

            if lo > hi: # i > j
                break

            self.swap(lo, hi)

        self.swap(pivot, hi)
        return hi

    def partitionAlternate(self, lo, hi):
        pivot, lo = lo, lo+1
        
        while lo <= hi:
            if self.nums[hi] < self.nums[pivot] < self.nums[lo]:
                self.swap(lo, hi)

            if self.nums[lo] <= self.nums[pivot]:
                lo += 1

            if self.nums[hi] >= self.nums[pivot]:
                hi -= 1

        self.swap(pivot, hi)
        return hi


qs = QuickSort([10, 12, 9, 6, 3, 7, 8])
print(qs.sort())

qs = QuickSort([1, 0, 1, 0, 0, 0, 1])
print(qs.sort())

qs = QuickSort([2, 2, 2, 2, 2])
print(qs.sort())

qs = QuickSort([2, 0, 2, 0, 0, 1, 2])
print(qs.sort())

qs = QuickSort([5, 4, 3, 2, 1])
print(qs.sort())

qs = QuickSort([1, 2, 3, 4, 5])
print(qs.sort())
