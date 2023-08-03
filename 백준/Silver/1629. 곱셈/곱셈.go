package main
import "fmt"

var known map[uint64]uint64

func main() {
    known = make(map[uint64]uint64)
    known[0] = 1
    var a, b, c uint64
    fmt.Scanln(&a, &b, &c)
    res := power(a % c, b, c)
    fmt.Println(res)
}

func power(a uint64, b uint64, c uint64) uint64 {
    if pow, ok := known[b]; ok {
        return pow
    }
    
    var res, pow uint64
    if (b % 2 == 0) {
        res = power(a, b / 2, c) % c
        pow = (res * res) % c
    } else {
        res = power(a, (b - 1) / 2, c) % c
        pow = (((res * res) % c) * a) % c
    }
    known[b] = pow
    return pow
}