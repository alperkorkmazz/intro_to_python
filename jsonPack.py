import json
#print(dir(json))
# json.load(f) -> load Json data from file
# json.load(s) -> load Json data from string
# json.dump(j,f) -> write JSON object to a file
# json.dumps(f) -> output JSON object as string
# some JSON:
json_file=open("data/json1.txt", "r", encoding="utf-8")
text_file=json.load(json_file)
json_file.close()
print(text_file)
print(type(text_file))
print(text_file.get("name"))
print(text_file.get("age"))
print(text_file.get("city"))
print(text_file["name"])
# create a json data
movie1 ={}
movie1["title"]="The Fifth Element"
movie1["director"]="Bruce Willis"
movie1["composer"]="Mike Hammer"
movie1["actors"]=["Bruce Willis","Samantha Path", "Eva Gerzegova"]
movie1["rate"]=8
movie1["Company"]="Warner Bros"
file2=open("data/json2.txt", "w", encoding="utf-8")
json.dump(movie1,file2,ensure_ascii=False)
file2.close()