import json

# Data to be written
dictionary = {
    "name": "yoonhee",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}
 
# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("sample.dic", "w") as outfile:
    outfile.write(json_object)

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}


# Writing to sample.json
with open("sample2.dic", "w") as outfile:
    outfile.write(json_object)

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 3100,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}
 
# Writing to sample.json
with open("sample3.dic", "w") as outfile:
    outfile.write(json_object)