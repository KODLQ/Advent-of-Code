import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from GetInput import getInput

getInput(2024, 2)


def createReport():
    report = []
    for row in open("input.txt").readlines():
        report.append(row.split())
    return report

def checkSafePart1(levels):
    increasing = int(levels[0]) < int(levels[1])

    for i in range(len(levels) - 1):
        if levels[i] == levels[i + 1]:
            return False
        if abs(int(levels[i]) - int(levels[i + 1])) > 3:
            return False
        if increasing and int(levels[i]) > int(levels[i+1]):
            return False
        if not increasing and int(levels[i]) < int(levels[i+1]):
            return False
    return True

def checkSafePart2(levels):
    unsafe = 0
    increasing = int(levels[0]) < int(levels[1])

    for i in range(len(levels) - 1):
        if levels[i] == levels[i + 1]:
            unsafe += 1
        if abs(int(levels[i]) - int(levels[i + 1])) > 3:
            unsafe += 1
        if increasing and int(levels[i]) > int(levels[i+1]):
            unsafe += 1
        if not increasing and int(levels[i]) < int(levels[i+1]):
            unsafe += 1
    return unsafe


def main():
    report = createReport()
    part1Count = 0
    part2Count = 0
    for i in range(len(report)):
        levels = report[i]
        unsafe1 = checkSafePart1(levels)
        unsafe2 = checkSafePart2(levels)

        if unsafe1:
            part1Count += 1
        if unsafe2 == 0 or unsafe2 == 1:
            part2Count += 1

    print(part1Count)
    print(part2Count)


if __name__ == "__main__":
    main()