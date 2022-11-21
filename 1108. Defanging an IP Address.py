address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# y = address.split(".")
# x = '[.]'.join(y)
# print(x)
res = '[.]'.join(address.split("."))
print(res)
# def defangIPaddr(adress):
    # return 