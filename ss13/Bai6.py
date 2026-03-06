numbers1 = [1,2,3]
numbers2 = [3,2,1]
if len(numbers1) == len(numbers2):
    print("Có cùng số giá trị")
else: 
    print("Khác số giá trị")
numbers1.sort()
numbers2.sort()
if numbers1 == numbers2:
    print("Giống cả giá trị phần tử")
else: 
    print("Khác về giá trị phần tử")