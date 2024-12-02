import bisect

def createLists():
    left = []
    right = []
    for row in open("input.txt").readlines():
        bisect.insort(left, row.split()[0])
        bisect.insort(right, row.split()[1])

    return left, right

def part1():
    left, right = createLists()
    dist = 0
    for i  in  range(len(left)):
        dist += abs(int(left[i]) - int(right[i]))

    print(dist)

def part2():
    left, right = createLists()
    dist = 0

    for i  in  range(len(left)):
        leftNum = int(left[i])
        count = 0
        for j in range(len(right)):
            if leftNum == int(right[j]):
                count += 1

        dist += (leftNum * count) 

    print(dist)



def main():
    part1()
    part2()


main()