str1=""
with open("images/sentence.svg") as file:
    for item in file:
        str1+=item
        # print(item)
print(str1)