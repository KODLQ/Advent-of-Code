def main():
    elfCalorieTotal, allElfCalorieTotal, top3ElfCalorieTotal = 0, [], []
    for row in open("../input.txt").readlines():
        if row == "\n":
            allElfCalorieTotal.append(elfCalorieTotal)
            elfCalorieTotal = 0
        else:
            elfCalorieTotal += int(row)
    for i in range(0,3):
        top3ElfCalorieTotal.append(max(allElfCalorieTotal))
        allElfCalorieTotal.remove(max(allElfCalorieTotal))
    print(f'Answer Part 1: {top3ElfCalorieTotal[0]}')
    print(f'Answer Part 2: {sum(top3ElfCalorieTotal)}')
    
if __name__ == '__main__':
    main()