file = open("in", "r")
lines = file.readlines()


def check(i, j):
    strings = []
    print(f"Checking {i}, {j}")
    try:
        strings.append("".join(lines[i][j:j+4]))
    except Exception as e:
        strings.append("error")
        print(f"Error processing str_r: {e}")

    try:
        strings.append(("".join(lines[i][j-3:j+1] if j-3 >= 0 else ""))[::-1])
    except Exception as e:
        strings.append("error")
        print(f"Error processing str_l: {e}")

    try:
        strings.append("".join((lines[x][j] if x >= 0 else "") for x in range(i-3, i+1))[::-1])
    except Exception as e:
        strings.append("error")
        print(f"Error processing str_u: {e}")

    try:
        strings.append("".join(lines[x][j] for x in range(i, i+4)))
    except Exception as e:
        strings.append("error")
        print(f"Error processing str_d: {e}")

    try:
        strings.append("".join((lines[i+x][j-x] if j-x >= 0 else "") for x in range(0,4)))
    except Exception as e:
        strings.append("error")
        print(f"Error processing str_dl: {e}")

    try:
        strings.append("".join(lines[i+x][j+x] for x in range(0,4)))
    except Exception as e:
        strings.append("error")
        print(f"Error processing str_dr: {e}")

    try:
        strings.append("".join((lines[i-x][j-x] if i-x >= 0 and j-x >=0 else "") for x in range(0,4)))
    except Exception as e:
        strings.append("error")
        print(f"Error processing str_ul: {e}")

    try:
        strings.append("".join((lines[i-x][j+x] if i-x >= 0 else "") for x in range(0,4)))
    except Exception as e:
        strings.append("error")
        print(f"Error processing str_ur: {e}")
    print("str_r, str_l, str_u, str_d, str_dl, str_dr, str_ul, str_ur")
    print (strings)
    return strings


def check2(i,j):
    if i - 1 < 0 or j - 1 < 0:
        return "error"
    else:
        try:
            return lines[i-1][j-1] + lines[i][j] + lines[i+1][j+1] + " "  + lines[i+1][j-1] + lines[i][j] + lines[i-1][j+1]
        except Exception as e:
            return "error"


def one():
    result = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] == "X":
                list = check(i, j)
                for string in list:
                    if string == "XMAS":
                        result += 1
    print(result)

def two():
    result = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] == "A":
                str = check2(i, j).split()
                if str[0] in ("MAS", "SAM") and str[1] in ("MAS", "SAM"):
                    print(str)
                    result += 1

    print(result)
two()
