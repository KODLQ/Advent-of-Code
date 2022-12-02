package main

import (
	"bufio"
	"fmt"
	"os"
)

func readFromFile(filePath string) []string {
	var fileLines []string

	readFile, err := os.Open(filePath)
	if err != nil {
		fmt.Println(err)
	}
	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		fileLines = append(fileLines, fileScanner.Text())
	}
	readFile.Close()
	return fileLines
}

func main() {
	fileLines := readFromFile("../input.txt")
	part1Total, part2Total, win, draw, lose, rock, paper, scissors := 0, 0, 6, 3, 0, 1, 2, 3
	part1Outcomes := map[string]int{
		"A X": draw + rock,
		"B X": lose + rock,
		"C X": win + rock,
		"A Y": win + paper,
		"B Y": draw + paper,
		"C Y": lose + paper,
		"A Z": lose + scissors,
		"B Z": win + scissors,
		"C Z": draw + scissors,
	}
	part2Outcomes := map[string]int{
		"A X": lose + scissors,
		"B X": lose + rock,
		"C X": lose + paper,
		"A Y": draw + rock,
		"B Y": draw + paper,
		"C Y": draw + scissors,
		"A Z": win + paper,
		"B Z": win + scissors,
		"C Z": win + rock,
	}

	for _, line := range fileLines {
		part1Total += part1Outcomes[line]
		part2Total += part2Outcomes[line]
	}

	fmt.Println("Answer Part 1:", part1Total)
	fmt.Println("Answer Part 2:", part2Total)
}
