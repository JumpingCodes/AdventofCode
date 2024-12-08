def read_input(file_name):
    eqations = []
    with open(file_name, "r") as f:
        for line in f:
            eqations.append(line.strip())
    return eqations


def return_nums(nums):
    result = []
    if len(nums) == 1:
        result.append(int(nums[0]))
        return result
    else:
        for num in return_nums(nums[1:]):
            result.append(int(nums[0])*int(num))
            result.append(int(nums[0])+int(num))
            result.append(int(str(num)+str(nums[0])))
        return result


def main():
    eqations = read_input("in")
    r = 0
    for eq in eqations:
        eq = eq.split(":")
        result = int(eq[0])
        values = eq[1].strip().split(" ")
        combinations = []
        combinations += return_nums(values[::-1])
        for combination in combinations:
            if result == combination:
                r += result
                break
    print(r)


if __name__ == "__main__":
    main()
