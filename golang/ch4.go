package main

import (
	"fmt"
	"errors"
)

func main(){
	// entries := []string{"the", "dog", "jumped", "over", "the", "chat", "box"}
	// listPrinter(entries)

	fakeStack := []int{0,1,2,3}
	fmt.Println(fakeStack)

	pushStack := pushStack(&fakeStack, 4)
	fmt.Println(pushStack)

	num, err := popStack(&fakeStack)
	if err != nil {
		fmt.Println(err)	
	}
	fmt.Println(num)
	fmt.Println(fakeStack)

	fakeStack = []int{100,200,300,400}
	fmt.Println(fakeStack)

	num, err = shiftStack(&fakeStack)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(num)
	fmt.Println(fakeStack)

	unShiftStack(&fakeStack, 150)
	fmt.Println(fakeStack)
}


func listPrinter(list []string){
	for _, word := range list {
		fmt.Println(word)
	}
}

func pushStack(customStack *[]int, num int)([]int){
	*customStack = append(*customStack, num)
	return *customStack
}

func popStack(customStack *[]int)(int, error){
	if len(*customStack) == 0 {
		return 0, errors.New("stack empty")
	}
	lastIndex := len(*customStack)-1
	num := (*customStack)[lastIndex]
	*customStack = (*customStack)[:lastIndex]
	return num, nil
}

func shiftStack(customStack *[]int)(int, error){
	if len(*customStack) == 0{
		return 0, errors.New("stack empty")
	}
	// return first element
	num := (*customStack)[0]
	*customStack = (*customStack)[1:]
	return num, nil
}

func unShiftStack(customStack *[]int, num int){
	// add element ot beginning
	*customStack = append([]int{num}, *customStack...)
}
