#!/usr/bin/env ruby

regex = /School/
input = ARGV[0]
puts "Input argument: #{input.inspect}"
puts input.scan(regex).join
