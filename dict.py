student = {
    "first_name": "Purity",
    "last_name": "Masanya",
    "gender": "Female",
    "age": 23,
    "marital status": "Single",
    "skills": ["Python", "HTML", "CSS"],
    "country": "Kenya",
    "city": "Kisumu",
    "address": "Kenya",
}


skills_value = student["skills"] #accessing the value of the key "skills"

student["skills"].append("JS") #adding a new skill to the list of skills

keys = student.keys() #accessing the keys of the dictionary

#del student #deleting the key "address" from the dictionary
#del student["city"] #deleting the key "city" from the dictionary


print(keys)
print(student)
print(type(skills_value)) #checking the type of the value of the key "skills"
print(student.items()) #accessing the items of the dictionary
