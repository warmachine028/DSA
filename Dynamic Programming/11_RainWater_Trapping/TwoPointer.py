# CODE 11c: Optimization of RainWater Trapping using 2 Pointer Approach


# Problem solution Using 2 Pointer
def trap(height: list[int]) -> int:  # Time Complexity: O(N)  Space Complexity: O(1)
    left = 0
    right = len(height) - 1
    l_max = r_max = 0
    water = 0
    while left <= right:
        current_height = min(height[left], height[right])
        if current_height == height[left]:  # .    left_height < right_height
            if current_height >= l_max:  # .       Calculating the maximum left Height
                l_max = current_height  # .        Can't Store water if current_height is the maximum height
            
            else:  # .                             If maximum height is found:
                water += l_max - current_height  # 1. Subtract current building height from max left height
                # .                                2. Add it to water
            left += 1  # .                         Incrementing Left Pointer
        else:
            if current_height >= r_max:  # .       Calculating the maximum right value
                r_max = current_height  # .        Cant store water if current_height is maximum height
            
            else:  # .                             If maximum height is found:
                water += r_max - current_height  # 1. Subtract current height from max_height
                # .                                2. Add it to water
            right -= 1  # .                        Decrementing Right Pointer
    
    return water  # .                              Finally return the quantity of water


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
print(trap([4, 2, 0, 3, 2, 5]))  # 9
