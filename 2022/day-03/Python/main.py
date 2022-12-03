def main():
    def getPrio(elem):
        return ord(elem) - ord('A') + 27 if elem.isupper() else ord(elem) - ord('a') + 1
    
    answer1, answer2 = 0, 0
    rugsacks = [row.rstrip() for row in open("./input.txt").readlines()]
    
    for rugsack in rugsacks:
        mid = len(rugsack)//2
        for prio in set(getPrio(elem) for elem in rugsack[:mid]) & set(getPrio(elem) for elem in rugsack[mid:]):
            answer1 += prio
    
    for i in range(2, len(rugsacks), 3):
        answer2 += getPrio(next(iter((set(rugsacks[i-2]) & set(rugsacks[i-1]) & set(rugsacks[i])))))
        
    print(f'Answer Part 1: {answer1}')
    print(f'Answer Part 2: {answer2}')

if __name__ == "__main__":
    main()