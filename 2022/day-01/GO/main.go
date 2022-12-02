package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
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

func maxWithIndex(slice []int) (int, int) {
	var largerNumber, temp int
	finalIndex := 0

	for i, element := range slice {
		if element > temp {
			temp = element
			largerNumber = temp
			finalIndex = i
		}
	}

	return largerNumber, finalIndex
}
func sum(array []int) int {
	result := 0

	for _, v := range array {
		result += v
	}

	return result
}

func removeIndex(s []int, index int) []int {
	return append(s[:index], s[index+1:]...)
}
func main() {
	elfCalorieTotal := 0
	var allElfCalorieTotal []int
	var top3ElfCalorieTotal []int

	for _, row := range readFromFile("../input.txt") {
		if row == "" {
			allElfCalorieTotal = append(allElfCalorieTotal, elfCalorieTotal)
			elfCalorieTotal = 0
		} else {
			calories, err := strconv.Atoi(row)
			if err != nil {
				fmt.Println(err)
			}
			elfCalorieTotal += calories
		}
	}

	for i := 0; i <= 2; i++ {
		max, index := maxWithIndex(allElfCalorieTotal)
		top3ElfCalorieTotal = append(top3ElfCalorieTotal, max)
		allElfCalorieTotal = removeIndex(allElfCalorieTotal, index)
	}

	fmt.Println("Answer Part 1:", top3ElfCalorieTotal[0])
	fmt.Println("Answer Part 2:", sum(top3ElfCalorieTotal))
}
