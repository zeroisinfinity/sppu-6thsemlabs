m = 45

if m < 10
  puts 10
elsif m < 20
  puts 20
elsif m < 30
  puts 30
else 
  puts 40
end

day = 2
case day
when 1
  puts 1
when 2 , 3 
  puts 2
else 
  puts 4
end

age = 12
case
when age > 10
  puts 12
else 
  puts 10
end

puts age >= 18 ? "Adult" : "Minor"
