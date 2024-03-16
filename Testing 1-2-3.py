# def number(lines):
#     lisbaru = []
#     if len(lines) == 0:
#         return []
#     else:
#         ind = 0
#         for i in range(len(lines)):
#             ind += 1
#             lisbaru.append("{}: {}".format(ind, lines[i]))
#         return lisbaru
def number(lines):
    return ["{}: {}".format(ind, line) for ind, line in enumerate(lines,start=1)]
print(number(["a", "b"]))