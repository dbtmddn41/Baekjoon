package main

import "fmt"

func main() {
	var score int
	var grade string

	fmt.Scanln(&score)
	switch {
	case score >= 90:
		grade = "A"
	case score >= 80:
		grade = "B"
	case score >= 70:
		grade = "C"
	case score >= 60:
		grade = "D"
	default:
		grade = "F"
	}
	fmt.Println(grade)
}