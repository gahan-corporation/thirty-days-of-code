import scala.concurrent.duration._

object Solution {
    def main(args: Array[String]) {
        // Print "Hello, World."
        println("Hello, World.")

        // Read a string variable
        val s = {
          val deadline = 5 seconds fromNow
          scala.io.StdIn.readLine()
        }

        // Print the value of the string variable
        println(s)
    }
}
