my_cat = ["salem", "black", "sassy"]

my_cat_dict = {
    "name":"salem",  # <- key vale pairs. name = Key. selem = vale. whole is an item.
    "colour":"black",
    "mood":"sassy"
}

# print(my_cat_dict["name"])

# print(my_cat_dict)  

My_pet = ["Marvs", "brown", "fluffy", "40%"] 

my_pet_dict = {
    "name":"Marvs",
    "colour":"brown",
    "fur":"fluffy",
    "how_annoying":"40%",
    "is_hungry":False
}

print(my_pet_dict)

my_pet_dict["is_hungry"] = True

print(my_pet_dict)

my_pet_dict["how_annoying"] = "60%"

print(my_pet_dict) 

print(my_pet_dict.keys())
print(list(my_pet_dict.keys())) 

for i in my_pet_dict():
    print(i) 

my_pet_dict.pop("how_annoying") 

print(my_pet_dict) 


countries = {
    "United Kingdom":"London",
    "France":"Paris",
    "Germany":"Berlin",
    "Spain":"Madrid",
    "Italy":"Rome"
}

fav_songs = [
    "Tears don't fall",
    "In the end",
    "Dead & buried",
    "Fall For You",
    "21 Guns"
]

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

dict_of_films = {
    "Sicario": 2008,
    "Arrival": 2011,
    "Dune": 2020,
    "Enemy": 2005,
    "Blade Runner 2049": 2018
}

list_of_films = [
    "Sicario",
    "Arrival",
    "Dune",
    "Enemy",
    "Blade Runner 2049"
]

print(list_of_films[0])

will_todo_dict = {
    "tired": True,
    "hungry": False,
    "exercise_time_day": 20,
    "homework": "Look at PEP 0484",
    "chores": "clean kitchen",
    6: 3.14152,

}

print(will_todo_dict)

will_todo_dict["chores"] = "None! All finished"

will_todo_dict["exercise_time_day"] = 110

print(will_todo_dict)

dict_of_dicts = {
    "dict1": {
        "key1": "value1",
        "key2": "value2"
    },
    "dict2": {
        "key3": "value3",
        "key4": "value4"
    }
}

print(dict_of_dicts["dict1"]["key1"])

dict_of_list = {
    "list1": [1, 2, 3, 4, 5],
    "list2": [6, 7, 8, 9, 10]
}

print(dict_of_list["list2"][-2])

