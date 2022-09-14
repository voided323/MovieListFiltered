import json


parseJson = open('movies.json')
jsonData = json.load(parseJson)
parseJson.close()

'''
Format needed by the assignment:
[
	{
		"name": "Forrest Gump",
		"year": 1994,
		"duration": 142,
		"genres": ["Drama", "Romance"]
	}.
	{
		etc
	}
]

'''

movies = []

for movie in jsonData['movies']:
	currObject = {"name": movie["title"],
				  "year": int(movie["year"]), 
				  "duration": int(movie["runtime"]),
				  "genres": movie["genres"] }
	movies.append(currObject)

outputFile = open('moviesPretty.json', 'w')
json.dump(movies, outputFile, indent=6)
outputFile.close()
