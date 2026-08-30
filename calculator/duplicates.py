ls = [1,2,2,'ali','mamad',3,4,4,4,'mamad']
duplicates = []
for i in range (len(ls)):
    if ls[i] not in duplicates:
        if ls[i] in ls[i+1:]:
            duplicates.append(ls[i])
print("duplicates:",duplicates)
# حذف آیتم‌های تکراری از لیست اصلی (به روش پشت‌سر)
for i in range(len(ls)-1, -1, -1):
    if ls[i] in duplicates:
        ls.pop(i)

print("لیست بدون تکراری‌ها:", ls)
