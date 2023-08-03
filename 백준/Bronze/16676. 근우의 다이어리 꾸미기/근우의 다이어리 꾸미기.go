package main

import (
	"fmt"
	"strconv"
)

func main() {	
	var N int64
	var threshold int64 = 1
	var res int

	fmt.Scanln(&N)
	str_N := strconv.FormatInt(N, 10)

	for i := 1; i < len(str_N); i++ {
		threshold *= 10
		threshold += 1
	}
	if N >= threshold || N == 0 {
		res = len(str_N)
	} else {
		res = len(str_N) - 1
	}
	fmt.Println(res)
}