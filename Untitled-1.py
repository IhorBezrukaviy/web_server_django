chars = "abcdefghijklmnopqrstuvwxyz"
check_string = "i am checking this string to see how many times each character appears"

# c=""
# cc=0

# for char in chars:
#     count = check_string.count(char)
#     if count > cc:
#         c=char
#         cc=count
#         print (c, cc)

d = dict.fromkeys(check_string, 0)
for c in check_string: 
    d[c] += 1
print (d)