nums = [1,2,3,4,1]
nums_1 = [1,2,3,4,5]

# for n in nums_1:
#     flag = False
#     if nums_1.count(n) > 1:
#         flag = True
#     else:
#         flag = False

# print(f"Flag: {flag}")

print(f"Duplicate Exists in the list: {len(nums_1) != len(set(nums_1))}")