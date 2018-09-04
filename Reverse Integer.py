def reverse(self, x):
    x = str(x)
    out = ""
    for m in reversed(range(len(x))):
        out += str(x[m])
    if out[-1] == '-':
        out = -int(out[:-1])
    else:
        out = int(out)
    if out < (-2)**31 or out > 2**31 - 1:
        return 0
    else:
        return out
# Input: -123
# Output: -321