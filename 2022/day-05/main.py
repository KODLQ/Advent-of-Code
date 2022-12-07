def parseInput(input):
    """
    Divide the input file to stacks and moves lists and returns as lists
    """
    (stacks, moves) = input.split("\n\n")
    stacks = [stack[1::4] for stack in stacks.split("\n")][:-1]
    stacks = list(zip(*stacks))
    stacks = [[crate for crate in elem if crate != " "] for elem in stacks]
    moves = [[action for action in move.split(" ")] for move in moves.split("\n")]
    return stacks, moves

def moveOneToOne(stacks, start, end, amount):
    """
    Moves first value from start stack to end stack the 
    given amount of times or until list is empty
    """
    for _ in range(min(len(stacks[start]), amount)):
        stacks[end].insert(0, stacks[start].pop(0))

    return stacks

def moveManyToOne(stacks, start, end, amount):
    """
    Moves amount of values from start stack to end stack keeping its order
    """
    for elem in stacks[start][0:amount][::-1]:
        stacks[end].insert(0, elem)
        stacks[start].pop(0)

    return stacks

def main():
    answer1, answer2 = "", ""
    (stacksPart1, moves) = parseInput(open("input.txt").read())
    (stacksPart2, moves) = parseInput(open("input.txt").read())
    for action in moves:
        start = int(action[3])-1
        end = int(action[5])-1
        amount = int(action[1])
        stacksPart1 = moveOneToOne(stacksPart1, start, end, amount)
        stacksPart2 = moveManyToOne(stacksPart2, start, end, amount)
    for stack in stacksPart1:
        answer1 += stack[0]
    for stack in stacksPart2:
        answer2 += stack[0]

    print(f'Answer Part 1: {answer1}')
    print(f'Answer Part 2: {answer2}')

if __name__=="__main__":
    main()