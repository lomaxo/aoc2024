data = '''2333133121414131402'''

with open("input/day9.txt") as file:
    data = file.read().strip()

def expand_disk_map(dm: str) -> list[str]:
    disk = []
    fileid=0
    is_space = False
    dm = list(dm)
    while dm:
        size = dm.pop(0)
        for _ in range(int(size)):
            if is_space:
                disk.append('.')
            else:
                disk.append(str(fileid))
        if not is_space:
            fileid += 1
        is_space = not is_space
    return disk


def compress_disk(disk):
    end_pointer = len(disk) - 1
    i = 0
    while True:
        # Get next empty space
        while disk[i] != '.':
            i += 1
            if i >= end_pointer:
                return disk
                

        # get next file from end
        while disk[end_pointer] == '.':
            end_pointer -= 1
            if i >= end_pointer:
                return disk

        disk[i] = disk[end_pointer]
        disk[end_pointer] = '.'
        # i += 1
        # end_pointer -= 1

    return disk

def calc_checksum(disk):
    total = 0
    for i in range(len(disk)):
        if disk[i] != '.':
            total += int(disk[i]) * i
    return total

disk = expand_disk_map(data)
disk = compress_disk(disk)
print(disk)
print(calc_checksum(disk))
 
