package main

import "fmt"

type ans_set struct {
	zero int
	one int
}

var known map[int] ans_set

func main() {
	var T int
	var N int
	known = make(map[int] ans_set)
    known[0] = ans_set{1, 0}
    known[1] = ans_set{0, 1}
    known[2] = ans_set{1, 1}

	fmt.Scanln(&T)
	for j := 0; j < T; j++ {
		fmt.Scanln(&N)
		ans := fibbo(N)
		fmt.Println(ans.zero, ans.one)
	}
}

func fibbo(N int) ans_set {
	if ans, ok := known[N]; ok {
        return ans
    }
	return add(fibbo(N-2), fibbo(N-3))
}

func add(a ans_set, b ans_set) ans_set {
	return ans_set{2*a.zero+b.zero, 2*a.one+b.one}
}