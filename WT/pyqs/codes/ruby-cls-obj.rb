class Classname
  #
end

class Student
  def initialize(name,age)
    @name = name
    @age = age
  end

  def display
    puts "Name : #{@name}"
    puts "Age : #{@age}"
  end

end

s1 = Student.new("Sahil",21)
s1.display


class Rec
  def initialize(len,bred)
    @len = len
    @bred = bred
  end

  def area
    @len * @bred
  end

end

r1 = Rec.new(10,5)
puts "Area : #{r1.area}"
