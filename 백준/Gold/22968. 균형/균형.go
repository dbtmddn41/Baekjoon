package main

import (
	"fmt"
)

func main() {
	var T int
	var V int
	delta := []int{1,2,3}
	height := []int{1, 2, 4}

	
	fmt.Scanln(&T)
	for t := 0; t < T; t++ {
		fmt.Scanln(&V)
		fmt.Println(search(V, &delta, &height))
		
	}
}

func search(V int, delta *[]int, height *[]int) int {
	for i := 0; ; i++ {
		for i < len((*height)) {
			if V < (*height)[i] {
				return i
			}
			i++
		}

		(*delta) = append((*delta), 2*(*delta)[i-2] + (*delta)[i-3])
		(*height) = append((*height), (*height)[i-1] + (*delta)[i-1]) 
		if V < (*height)[i] {
			return i
		}
	}
}