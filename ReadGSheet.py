import gspread

gc = gspread.service_account(filename='cred.json')
sh = gc.open_by_key('1Ujqtjm6-F5VO3dhi3fehOCQoFtL8xvEihadRdPAajc8')
worksheet = sh.sheet1
max_cols = len(worksheet.col_values(1))

print(f"{max_cols} lines in this lesson today. What's your range for today?\n")

a = input("range? ")
c = input("range? ")
res = worksheet.get(a)
res2 = worksheet.get(c)

lst = []

for line in res:
    lst.append(line)
for line2 in res2:
    lst.append(line2)    
for b, x in zip(res, res2):
    print(f"\nwhat does this mean? {b}")
    input()
    print(f"The correct answer is: {x}")
    ele = input("\nDid you get it right? y or n: ")
    lst.append(ele)
print(f"Your score is {lst.count('y')} out of {lst.count('n') + lst.count('y')}\nWell Done!! ")