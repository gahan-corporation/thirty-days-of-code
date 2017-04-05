package main

import (
  "bufio"
  "fmt"
  "os"
  "time"
)

func main() {

  reader := bufio.NewReader(os.Stdin)
  //text, _ := reader.ReadString('\n')

  fmt.Println("Hello, World.")

  for {
    select {
    case i := <-input:
        fmt.Println(i)
    case <-time.After(4000 * time.Millisecond):
        fmt.Println("There weren't no input.")
    }
  }
}
