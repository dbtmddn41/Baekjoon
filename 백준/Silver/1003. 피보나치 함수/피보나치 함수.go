package main

import "fmt"

type ans_set struct {
	zero int
	one int
}


func main() {
	var T int
	var N int
	var known map[int] ans_set
	known = make(map[int] ans_set)
    known[0] = ans_set{1, 0}
    known[1] = ans_set{0, 1}
    known[2] = ans_set{1, 1}

	fmt.Scanln(&T)
	for j := 0; j < T; j++ {
		fmt.Scanln(&N)
		ans := fibbo(N, known)
		fmt.Println(ans.zero, ans.one)
	}
}

func fibbo(N int, known map[int]ans_set) ans_set {
	if ans, ok := known[N]; ok {
        return ans
    }
	res1 := fibbo(N-2, known)
	res2 := fibbo(N-3, known)
	known[N] = add(&res1, &res2)
	return known[N] 
}

func add(a *ans_set, b *ans_set) ans_set {
	return ans_set{2*a.zero+b.zero, 2*a.one+b.one}
}