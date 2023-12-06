# 3 лаба доп

string_ = input().split()
letter_ = input()
print(*[i for i in string_ if i[0] == letter_])
# for element in string_:
#     if element[:len(letter_)] == letter_:
#         print(element)