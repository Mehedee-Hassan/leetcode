from typing import List


class Solution:

    def __init__(self, DEBUG_MODE: bool = False):
        self.DEBUG_MODE = DEBUG_MODE

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        save = {}
        largest = 0

        i = 0
        last_pos = -1

        for num in nums:

            if num in save:
                save[num] += 1
            else:
                save[num] = 1

            while save[num] > k:
                # upto this point it was contiguous for less than or
                # equal to k

                last_pos += 1
                save[nums[last_pos]] -= 1
            if largest <= (i - last_pos):
                largest = i - last_pos
            if self.DEBUG_MODE:
                print("[DEBUG] inside loop ", save, " ", last_pos)
                print("[DEBUG] largest = ", largest)

            i += 1

        return largest
