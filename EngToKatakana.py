string = "bow"
string2 = string.replace("y", "i")  # replace all
li = list(string2)
vol = {"a", "e", "u", "i", "o", "-"}
th = {"t", "s", "c"}

i = 0
while i < len(li):
    if i <= len(li) - 2:
        if (li[i] in vol) and (li[i + 1] in vol):  # doubel vol
            if li[i] == "e" and li[i + 1] == "a":
                li[i] = "i"
                li[i + 1] = "-"
                i = i + 2
            elif li[i] == "e" and li[i + 1] == "e":
                li[i] = "i"
                li[i + 1] = "-"
                i = i + 2
            elif li[i] == "o" and li[i + 1] == "o":
                li[i] = "u"
                li[i + 1] = "-"
                i = i + 2
            else:
                i = i + 1
        elif (i <= len(li) - 3) and (li[i] in vol) and (li[i + 2] in vol):
            if li[i] == "a":
                li[i] = "e"
                li.insert(i + 1, "i")
                i = i + 2
            elif li[i] == "e":
                li[i] = "i"
                li.insert(i + 1, "-")
                i = i + 2
            elif li[i] == "u":
                li[i] = "i"
                li.insert(i + 1, "u")
                i = i + 2
            elif li[i] == "i":
                li[i] = "a"
                li.insert(i + 1, "i")
                i = i + 2
            elif li[i] == "o":
                li.insert(i + 1, "u")
                i = i + 2
        else:
            i = i + 1
    elif li[i] == "e":  # open with e
        if li[i - 2] in vol:
            li.pop()
        else:
            li[i] = "i"
            li.insert(i + 1, "-")
            i = i + 2
    else:
        i = i + 1

newstr = ''.join(li)
print(newstr)
