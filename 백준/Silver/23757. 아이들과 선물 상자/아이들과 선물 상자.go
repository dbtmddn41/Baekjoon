// This example demonstrates an integer heap built using the heap interface.
package main

import (
	"container/heap"
	"fmt"
	"bufio"
	"os"
	"strconv"
)

// An IntHeap is a min-heap of ints.
type Maxheap []int

func (h Maxheap) Len() int           { return len(h) }
func (h Maxheap) Less(i, j int) bool { return h[i] > h[j] }
func (h Maxheap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *Maxheap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *Maxheap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
func (h *Maxheap) update(value int) {
    heap.Fix(h, value)
}

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	scanner = bufio.NewScanner(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()
	scanner.Split(bufio.ScanWords)

	var N, M int
	var childs []int

	N, M = scanInt(), scanInt()
	gifts := &Maxheap{}
	heap.Init(gifts)
	for i := 0; i < N; i++ {
		heap.Push(gifts, scanInt())
	}

	for i := 0; i < M; i++ {
		childs = append(childs, scanInt())
	}

	res := 1
	for _, child := range childs {
		gift := heap.Pop(gifts).(int)
		if gift < child {
			res = 0
			break
		} else if gift > child {
			heap.Push(gifts, gift - child)
		}
	}
	fmt.Fprintln(writer, res)
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