package main

import(
	"fmt"
)

func solve(a []int, b []int) int{
    var count int
    count = 0
    for i:=0; i < len(a); i++{
    	if i == 0{
    		if a[i] >= b[i]{
    			count++
    		}
    	}else{
    		if a[i] - a[i - 1] >= b[i]{
    			count++
    		}
    	}
    }
    return count
}

// https://www.codechef.com/problems/ATM2

func main(){
	var t int
	fmt.Scanln(&t)
	var i = 0
	for i < t{
		var n int
		fmt.Scan(&n)
		var a = make([]int, n)
		var b = make([]int, n)
		for j:=0; j < n; j++{
			fmt.Scan(&a[j])
		}
		for k:=0; k < n; k++{
			fmt.Scan(&b[k])
		}
		var ans = solve(a,b)
		fmt.Println(ans)
		i++
	}
}
