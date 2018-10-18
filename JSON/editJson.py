import json
#import io

with open("hello.txt",mode="w",encoding="utf-8") as files:
	files.write("凹凹\n12\n3")
	
with open("test.json",mode="r",encoding="utf8") as files:
	jsonData=json.load(files)
	print("name : ",jsonData["name"])
	print("ver : ",jsonData["ver"])
	jsonData["name"]=jsonData["name"]+" re"
with open("test.json",mode="w",encoding="utf8") as files:
	json.dump(jsonData,files)