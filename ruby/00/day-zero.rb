require 'timeout'

# Print a string literal saying "Hello, World." to stdout.
puts 'Hello, World.'

begin
  Timeout::timeout(1) do
    input_string = gets
  end

rescue Timeout::Error
  puts "There weren't no input."
end
