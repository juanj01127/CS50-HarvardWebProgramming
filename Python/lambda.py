people=[
    {"name":"Harry" , "house":"Gryffindor"},
    {"name":"Cho" , "house":"RavenClaw"},
    {"name":"Draco" , "house":"Slythrin"}
]

people.sort(key=lambda person: person["name"])

print(people)