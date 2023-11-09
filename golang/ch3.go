package main

import "fmt"

func main(){
	// fmt.Println(square(3))

	// fmt.Println(minimum(3, 9))

	fmt.Println(charCounter("aab;lksjdfoiwea", "a"))
}

func square(num int)(int){
	return num * num
}

func minimum(numA, numB int)(int){
	if numA < numB {
		return numA
	}
	return numB
}

// function that counts the occurance of a target char in a string
func charCounter(str, target string)(int){
	counter := 0

	for i:= 0; i<len(str); i++ {
		if string(str[i]) == target{
			counter += 1
		}
	}
	return counter
}

