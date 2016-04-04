package main

func main() {
    for x := 1; x < 101; x++ {
        if x%3 < 1        { print("Fizz") }
        if x%5 < 1        { print("Buzz") }
        if x%5>0 && x%3>0 { print(x)      }
        println()
    }
}
