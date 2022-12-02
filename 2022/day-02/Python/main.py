def main():
    part1Total, part2Total, win, draw, lose, rock, paper, scissors = 0, 0, 6, 3, 0, 1, 2, 3
    part1Outcome = {
        "A X" : draw+rock,
        "B X" : lose+rock,
        "C X" : win+rock,
        "A Y" : win+paper,
        "B Y" : draw+paper,
        "C Y" : lose+paper,
        "A Z" : lose+scissors,
        "B Z" : win+scissors,
        "C Z" : draw+scissors
    }
    part2Outcome = {
        "A X" : lose+scissors,
        "B X" : lose+rock,
        "C X" : lose+paper,
        "A Y" : draw+rock,
        "B Y" : draw+paper,
        "C Y" : draw+scissors,
        "A Z" : win+paper,
        "B Z" : win+scissors,
        "C Z" : win+rock
    }
    for row in open("../input.txt").readlines():
        part1Total+=part1Outcome[row[:-1]]
        part2Total+=part2Outcome[row[:-1]]
    print(f'Answer Part 1: {part1Total}')
    print(f'Answer Part 2: {part2Total}')

if __name__ == '__main__':
    main()