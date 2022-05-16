fav_songs_dict = [
    {"artist":"Bullet for my Valentine",
    "song":"Tears don't fall",
    "release year": "2005",
    "genre": "alternative/indie"
    },
    {"artist":"Black veil brides",
    "song":"In the end",
    "release year": "2013",
    "genre": "Metal"
    },
    {"artist":"A day to remember",
    "song":"Dead & buried",
    "release year": "2013",
    "genre": "alternative/indie"
    },
    {"artist":"Secondhand Serenade",
    "song":"Fall For You",
    "release year": "2008",
    "genre": "alternative/indie"
    },
    {"artist":"green day",
    "song":"21 Guns",
    "release year": "2009",
    "genre": "alternative/indie"
    } 
]
empty = [] 

for i in fav_songs_dict:  
    empty.append(list(i.values())[0])

def add_to_list(band):
    empty.append(band)

# def del_from_list():
#     empty.remove(band)

