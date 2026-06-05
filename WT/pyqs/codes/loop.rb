i = 1
while i < 9
  i += 1
  #next if i == 3
  puts i
end

j = 9
until j > 3
  #break if j == 5
  puts j
  i -= 1
end

for k in 1..5
  #redo if k == 3
  puts k
end

[1,2,3].each do |i|
  puts i
end


