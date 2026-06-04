import json

student = {"name": "Megha"}

file = open("student.json", "w")
json.dump(student, file)
file.close()

print("Saved")
