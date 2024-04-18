def intersect(nums1, nums2):
    # Create a hash map to count occurrences of elements in nums1
    count_map = {}
    for num in nums1:
        count_map[num] = count_map.get(num,0)+1

    # Find the intersection
    intersection = []
    for num in nums2:
        if num in count_map and count_map[num] > 0:
            intersection.append(num)
            count_map[num] -= 1  # Decrease count for found element

    return intersection

if __name__ == "__main__":

# Example usage
 nums1 = [1, 2, 2, 1]
 nums2 = [2, 2]
 print(intersect(nums1, nums2))  # Output: [2,2]

 nums1 = [4, 9, 5]
 nums2 = [9, 4, 9, 8, 4]
 print(intersect(nums1, nums2))  # Output: [4,9] or [9,4] depending on the hash map's order
