


nums = [4, 7, 1, 3, 9, 3]
min_length = float("inf")
current_sum = 0
left = 0
right = 0
s = 57


for right, num in enumerate(nums):
    current_sum += num  # increment the sum
    while current_sum >= s:  # is the current sum at least the value of S?
        min_length = min(
            min_length, left + 1
        )  # shrink the window by brining in the left edge
        current_sum -= nums[
            left
        ]  # decrement the sum by the value on the left edge of the window
        left += 1  # update the pointer marking the left edge of the window
