package main

import "fmt"


var known map[int] [2]int

func main() {
	var T int
	var N int
	known = make(map[int] [2]int)
    known[0] = [2]int{1, 0}
    known[1] = [2]int{0, 1}
    known[2] = [2]int{1, 1}

	fmt.Scanln(&T)
	for j := 0; j < T; j++ {
		fmt.Scanln(&N)
		ans := fibbo(N)
		fmt.Println(ans[0], ans[1])
	}
}

func fibbo(N int) [2]int {
	if ans, ok := known[N]; ok {
        return ans
    }
	return add(fibbo(N-2), fibbo(N-3))
}

func add(a [2]int, b [2]int) [2]int {
	return [2]int{2*a[0]+b[0], 2*a[1]+b[1]}
}