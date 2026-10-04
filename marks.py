student_name = input("Enter student name: ")
maths_marks = int(input("Enter Maths marks: "))
science_marks = int(input("Enter Science marks: "))
english_marks = int(input("Enter English marks: "))
telugu_marks = int(input("enter telugu marks: "))
total = maths_marks + science_marks + english_marks+telugu_marks
percentage = (total /400)* 100
print("Student Name:", student_name)
print("Maths Marks:", maths_marks)
print("Science Marks:", science_marks)
print("English Marks:", english_marks)
print("Telugu marks:",telugu_marks)
print("Total:",total)
print("Percentage:",percentage)

