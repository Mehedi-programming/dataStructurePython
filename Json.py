import json
json_data = '{"name": "Mehedi", "age": 25, "student":123}'
data = json.loads(json_data)
print(type(json_data))
print(data)
print(type(data))


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
print(type(x))
print(x['name'])

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print(type(y))
print(y[2:6])


python_data = {
    "name": "Mehedi",                 
    "age": 25,                        
    "cgpa": 3.75,                      
    "is_student": True,                
    "is_graduated": False,           
    "skills": ["Python", "Django"],   
    "marks": (90, 85, 88),            
    "details": {                       
        "university": "DU",
        "year": 2024
    },
    "hobbies": None                    
}

# Python → JSON
json_data = json.dumps(python_data, indent=4)
print(json_data)


# json to python

json_data = '''
{
    "name": "Mehedi",
    "age": 25,
    "is_student": true,
    "marks": {"bangla":88,"english":99,"math":78},
    "details": {
        "department": "CSE",
        "passed": false
    },
    "hobbies": null
}
'''

# ✅ JSON → Python
python_data = json.loads(json_data)


print(python_data)
print(type(python_data))  # <class 'dict'>


print(python_data["name"])
print(python_data["marks"]['bangla'])  
print(python_data["details"]["department"])  
print(python_data["hobbies"])     
