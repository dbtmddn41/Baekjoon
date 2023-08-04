package main

import (
	"fmt"
	"bufio"
	"os"
	"strconv"
	"math"
	"sort"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	scanner = bufio.NewScanner(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

var (
	N int
	A []int
)

func main() {
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)

	setInput()
	ans := solve()

	fmt.Fprintln(writer, ans)
}

func solve() int {
	var ans int
	sort.Ints(A)

	for i := 0; i < (len(A)+1) / 2; i++ {
		ans += int(math.Floor(math.Log2(float64(A[i]))))
	}
	return ans + 1
}

func setInput() {
	N = scanInt()
	for i := 0; i < N; i++ {
		A = append(A, scanInt())
	}
}

func scanString() string {
	scanner.Scan()
	return scanner.Text()
}

func mustParseInt(s string) int {
	n, _ := strconv.Atoi(s)
	return n
}

func scanInt() int {
	return mustParseInt(scanString())
	// n, _ = strconv.Atoi(scanner.Scan().Text())
	// return n
}
