package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func main() {
	str0 := "input"
	var arr0 []int
	c := 0
	for _,val:= range strings.Split(str0, "\n"){
		i, err := strconv.Atoi(strings.TrimSpace(val))
		if err != nil {
			arr0 = append(arr0, c)
			c = 0
			continue
		} else {
			c += i
		}		
	}
	sort.Ints(arr0)
	fmt.Println(arr0[len(arr0)-1], arr0[len(arr0)-1]+arr0[len(arr0)-2]+arr0[len(arr0)-3])
}
