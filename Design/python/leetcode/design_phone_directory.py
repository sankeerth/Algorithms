"""
379. Design Phone Directory

Design a phone directory that initially has maxNumbers empty slots that can store numbers. The directory should store numbers, 
check if a certain slot is empty or not, and empty a given slot.
Implement the PhoneDirectory class:
PhoneDirectory(int maxNumbers) Initializes the phone directory with the number of available slots maxNumbers.
int get() Provides a number that is not assigned to anyone. Returns -1 if no number is available.
bool check(int number) Returns true if the slot number is available and false otherwise.
void release(int number) Recycles or releases the slot number.

Example 1:
Input
["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
[[3], [], [], [2], [], [2], [2], [2]]
Output
[null, 0, 1, true, 2, false, null, true]
Explanation
PhoneDirectory phoneDirectory = new PhoneDirectory(3);
phoneDirectory.get();      // It can return any available phone number. Here we assume it returns 0.
phoneDirectory.get();      // Assume it returns 1.
phoneDirectory.check(2);   // The number 2 is available, so return true.
phoneDirectory.get();      // It returns 2, the only number that is left.
phoneDirectory.check(2);   // The number 2 is no longer available, so return false.
phoneDirectory.release(2); // Release number 2 back to the pool.
phoneDirectory.check(2);   // Number 2 is available again, return true.

Constraints:
1 <= maxNumbers <= 104
0 <= number < maxNumbers
At most 2 * 10^4 calls will be made to get, check, and release.
"""


class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.maxNumbers = maxNumbers
        self.used = set()
        self.freed = list()

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if len(self.used) == self.maxNumbers:
            return -1
        if not self.freed:
            res = len(self.used)
        else:
            res = self.freed.pop(0)
        
        self.used.add(res)
        return res

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        if number in self.used:
            return False
        return True

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number not in self.used:
            return
        self.used.remove(number)
        self.freed.append(number)


ph = PhoneDirectory(3);
ph.get()
ph.get()
ph.check(2)
ph.get()
ph.check(2)
ph.release(2)
ph.check(2)


"""
use an array next[] to store the next available number.
when a number k is issued, move pointer pos = next[k] to the next available position. set next[k]=-1 and
when a number is recycled, sipmly move pointer from pos to the recycled number, and change the recycled number's "next" point to pos.

class PhoneDirectory {

    /** Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    int[] next;
    int pos;
    public PhoneDirectory(int maxNumbers) {
        next = new int[maxNumbers];
        for (int i=0; i<maxNumbers; ++i){
            next[i] = (i+1)%maxNumbers;
        }
        pos=0;
    }
    
    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    public int get() {
        if (next[pos]==-1) return -1;
        int ret = pos;
        pos = next[pos];
        next[ret]=-1;
        return ret;
    }
    
    /** Check if a number is available or not. */
    public boolean check(int number) {
        return next[number]!=-1;
    }
    
    /** Recycle or release a number. */
    public void release(int number) {
        if (next[number]!=-1) return;
        next[number] = pos;
        pos = number;
    }
}
"""
