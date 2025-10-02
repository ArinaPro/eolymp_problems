
# here are my eolymp task that I have done sinse 02/10/2025 (date/month/year)

# 5058

n = input()
opening_layers = {"(": [], "{": [], "[": []}
brackets = {")":"(", "}":"{", "]":"["}
i = 0 # layers
res = "yes"
for br in n:
    if br in opening_layers.keys():
        opening_layers[br].append(i)
        i += 1
    else:
        l = opening_layers[brackets[br]]
        if len(l) != 0:
            if i-1 == l[len(l)-1]:
                i -= 1
                l = l[:len(l)-1]
                opening_layers[brackets[br]] = l
            else:
                res = "no"
                break
        else:
            res = "no"
            break
for l_br in opening_layers.values():
    if len(l_br) != 0:
        res = "no"
print(res)




