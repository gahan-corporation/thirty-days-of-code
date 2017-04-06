package main

import (
  "bufio"
  "fmt"
  "os"
  "time"
)

func getInput(input chan string) {
  for {
    in := bufio.NewReader(os.Stdin)
    result, _ := in.ReadString('\n')
    input <- result
  }
}

func main() {
  input := make(chan string, 1)
  go getInput(input)

  fmt.Println("Hello, World.")
  select {
  case i := <-input:
      fmt.Println(i)
  case <-time.After(100 * time.Millisecond):
      fmt.Println("There weren't no input.")
  }
}
