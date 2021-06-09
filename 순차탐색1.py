# def search_list(a, x):
#     n = len(a)
#     for i in range(n):
#         if x[i] == a[i]:
#             return x[i]
#     return '?'

# stu_no = [39, 14, 67, 105]
# stu_name = ['Justin', 'John', 'Mike', 'Summer']

# print(search_list(stu_no, stu_name))

# d = {"Justin": 13, "John": 10, "Mike": 9}
# print(d["Mike"])
#
# d["summer"] = 1
# print(d["summer"])

stuInfo = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}

def findStu(num):
    if num in stuInfo:
        return stuInfo[num]
    else:
        return "?"

print(findStu(14)) #John
print(findStu(68)) #?