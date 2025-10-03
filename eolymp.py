
# here are my eolymp task that I have done sinse 02/10/2025 (date/month/year)

# 5058

# n = input()
# opening_layers = {"(": [], "{": [], "[": []}
# brackets = {")":"(", "}":"{", "]":"["}
# i = 0 # layers
# res = "yes"
# for br in n:
#     if br in opening_layers.keys():
#         opening_layers[br].append(i)
#         i += 1
#     else:
#         l = opening_layers[brackets[br]]
#         if len(l) != 0:
#             if i-1 == l[len(l)-1]:
#                 i -= 1
#                 l = l[:len(l)-1]
#                 opening_layers[brackets[br]] = l
#             else:
#                 res = "no"
#                 break
#         else:
#             res = "no"
#             break
# for l_br in opening_layers.values():
#     if len(l_br) != 0:
#         res = "no"
# print(res)


# 2099


# n = int(input())
# nl = input().split()
# m = int(input())
# ml = input().split()
# res = []
#
# for l in nl:
#     if l not in ml:
#         res.append(l)
# print(len(res))
# for r in range(len(res)):
#     if r != len(res)-1:
#         print(res[r], end=" ")
#     else:
#         print(res[r])


# 4847

from sys import stdin

res = dict()
for _ in range(7):
    a = input()
    action = a.split()
    if action[0] != "POP":
        res.update({action[1]:action[2]})
    else:
        m = list(res.values()).index(max(res.values()))
        print(f"{list(res.keys())[m]} {res[list(res.keys())[m]]}")
        res.pop(list(res.keys())[m])
# for r in range(len(res)):
#     if r != len(res)-1:
#         print(f"{list(res.keys())[r]} {list(res.values())[r]}", end=" ")
#     else:
#         print(f"{list(res.keys())[r]} {list(res.values())[r]}")
