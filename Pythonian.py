
numgrades=float(input("how many grades: "))
counter = 0

grades = []
while counter< numgrades:
	grades.append(input("please enter grade"))
	counter += 1
for grade in range(len(grades)):
	if(grades[grade]<60):
		print("Your grade is an F.")
	elif(grades[grade]>=60 and grade<70):
		print("Your grade is an D[.")
	elif(grades[grade]>=70 and grade<80):
		print("Your grade is an C.")
	elif(grades[grade]>=80 and grade<90):
		print("Your grade is an B.")
	elif(grades[grade]>=90):
		print("Your grade is an A.")

