package main

import "fmt"

func main(){
	fmt.Println("start")

	// makeTriangle(7)

	// fizzbuzz()

	// fmt.Println(makeBoardGame(3))
	// fmt.Println(makeBoardGame(20))

}

func makeTriangle(size int){
	triangle := ""
	for i:= 0; i<size; i++ {
		triangle += "#"
		fmt.Println(triangle)
	}
}

// For numbers divisible by 3, print "Fizz" instead of the number, 
// and for numbers divisible by 5 (and not 3), print "Buzz" instead.
func fizzbuzz(){
	fizz := "Fizz"
	buzz := "Buzz"

	for i:=0; i<20; i++ {
		if i % 3 == 0 && i % 5 == 0 {
			fmt.Println(fizz + buzz)
		} else if i % 3 == 0 {
			fmt.Println(fizz)
		} else if i % 5 == 0 {
			fmt.Println(buzz)
		} else {
			fmt.Println(i)
		}
	}

}

// make a dynamically sized chess board
func makeBoardGame(size int)(string){
	white := " "
	black := "#"
	newLine := "\n"
	board := ""

	rowA := ""
	rowB := ""

	for i:=0; i<size; i++ {
		if i % 2 == 0 {
			rowA += white
			rowB += black
		} else {
			rowA += black
			rowB += white
		}
	}

	for i:=0; i<size; i++ {
		if i % 2 == 0 {
			board += rowA + newLine
		} else {
			board += rowB + newLine
		}
	}
	return board
}
