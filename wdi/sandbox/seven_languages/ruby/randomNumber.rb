hidden = rand(10)

puts "guess the number"
guess = gets.to_i

if  guess == hidden
  puts "correct!"
elsif guess > hidden
  puts "lower"
else
  puts "higher"
end
