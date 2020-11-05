def removeDuplicates(nums):
    new_list = []
    for i in range(len(nums)):
        if nums[i] not in new_list:
            new_list.append(nums[i])
            length = len(new_list)
    print(f"Length = {length}")


removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
