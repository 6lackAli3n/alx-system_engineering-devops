#!/usr/bin/env ruby
# Ensure that there's exactly one argument provided
unless ARGV.length == 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit(1)
end

regex = /hb{0,1}tn/

match = ARGV[0].match(regex)

# Output the matched string if there's a match, otherwise print nothing
puts match ? match[0] : ""
