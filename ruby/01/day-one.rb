#!/usr/bin/env ruby

require 'timeout'

i = 4
d = 4.0
s = "Run's house "

j = 0
e = 0.0
t = ""

begin
  Timeout::timeout(1) do
    j = gets

    k = i + j.to_i

    puts k
  end

  Timeout::timeout(1) do
    e = gets

    f = d + e.to_f
    
    puts f
  end

  Timeout::timeout(1) do
    t = gets

    u = s + t

    puts u 
  end

rescue Timeout::Error
  puts "There weren't no input."
end
