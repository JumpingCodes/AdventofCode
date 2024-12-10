def read_input(file_name) -> list:
    with open(file_name, "r") as f:
        list = []
        for line in f:
            for x in line.strip():
                list.append(int(x))
        return list

def translate_input(list) -> list:
    translated_list=[]
    current_num = 0

    for i in range(0, len(list)):
        if i % 2 == 0:
            for j in range(0, list[i]):
                translated_list.append(current_num)
            current_num += 1
        else:
            for j in range(0, list[i]):
                translated_list.append(".")
    return translated_list

def rearange_list(list) -> list:
    i = 0
    j = len(list) - 1
    while(i < j):
        if list[i] != '.':
            i += 1
            continue
        if list[j] == '.':
            j -= 1
            continue
        list[i] = list[j]
        list[j] = '.'
    return list


def get_blocks(list) -> list:
    blocks = []
    start_pointer = 0
    search_pointer = 0
    while start_pointer < len(list):
        while list[start_pointer] == list[search_pointer] and search_pointer < len(list) - 1 and list[search_pointer + 1] == list[search_pointer]:
            search_pointer += 1
        if list[start_pointer] != '.':
            blocks.append([list[start_pointer], start_pointer, search_pointer])

        search_pointer += 1
        start_pointer = search_pointer
    blocks.pop(0)
    return blocks

def get_spaces(list, block_start) -> list:
    spaces = []
    start_pointer = 0
    search_pointer = 0
    while start_pointer < len(list):
        while list[start_pointer] == list[search_pointer] and search_pointer < len(list) - 1 and list[search_pointer + 1] == list[search_pointer]:
            search_pointer += 1
        if list[start_pointer] == '.' and search_pointer < block_start:
            spaces.append([list[start_pointer], start_pointer, search_pointer])
        search_pointer += 1
        start_pointer = search_pointer
    return spaces

def defragment_list(list) -> list:
    blocks = get_blocks(list)

    while(blocks != []):

        b = len(blocks) - 1
        block_start = blocks[b][1]
        spaces = get_spaces(list, block_start)

        print("wokring on " + str(b))
        if blocks == [] or spaces == []:
            break
        space_id = - 1
        block_size = (blocks[b][2] - blocks[b][1])

        for s in range(0, len(spaces)):
            current_space_size = (spaces[s][2] - spaces[s][1])
            if current_space_size >= block_size:
                space_id = s
                break

        if space_id == -1:
            blocks.pop(b)
            continue

        for w in range(spaces[space_id][1], spaces[space_id][1] + block_size + 1):
            list[w] = blocks[b][0]
        for w in range(blocks[b][1], blocks[b][2] + 1):
            list[w] = '.'

        spaces.pop(space_id)
        blocks.pop(b)
    return list


def calculate_checksum(list) -> int:
    sum = 0
    for i in range(0, len(list)):
        if list[i] == '.':
            continue
        sum += i * list[i]
    return sum

def main():
    line = list(read_input("in"))
    translated_list = translate_input(line)
    #rearanged_list_1 = rearange_list(translated_list)
    defragmented_list = defragment_list(translated_list)
    print(calculate_checksum(defragmented_list))


if __name__ == "__main__":
    main()
