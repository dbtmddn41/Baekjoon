// This example demonstrates an integer heap built using the heap interface.
package main

import (
	"container/heap"
	"fmt"
	"bufio"
	"os"
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

// This example inserts several ints into an Maxheap, checks the minimum,
// and removes them in order of priority.
func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var N, M int
	var childs []int
	var tmp int

	fmt.Fscanln(reader, &N, &M)
	gifts := &Maxheap{}
	heap.Init(gifts)
	for i := 0; i < N; i++ {
		fmt.Fscan(reader, &tmp)
		heap.Push(gifts, tmp)
	}

	for i := 0; i < M; i++ {
		fmt.Fscan(reader,&tmp)
		childs = append(childs, tmp)
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
