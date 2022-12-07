def main():
    answer1, answer2 = 0, 0
    assignmentPairs = [row.rstrip() for row in open("./input.txt").readlines()]
    for pair in [ tuple(elem.split(',')) for elem in assignmentPairs ]:
        elf1 = pair[0].split('-')
        elf2 = pair[1].split('-')
        elf1Set = set([ i for i in range(int(elf1[0]), int(elf1[1])+1) ])
        elf2Set = set([ i for i in range(int(elf2[0]), int(elf2[1])+1) ])
        if elf1Set.issubset(elf2Set) or elf2Set.issubset(elf1Set):
            answer1+=1
        for pair in elf1Set:
            if pair in elf2Set:
                answer2+=1
                break
            
    print(f'Answer Part 1: {answer1}')
    print(f'Answer Part 2: {answer2}')

if __name__ == "__main__":
    main()