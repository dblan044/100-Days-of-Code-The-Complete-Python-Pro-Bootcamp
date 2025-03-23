#Dictionary access
travel_logs = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Stuttgart"],
}
print(travel_logs["France"][2])

#Nested List access
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

#Nested dictionary in a dictionary
travel_logs_2 = {
    "France":{
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": [5]
    },
    "Germany":{
        "cities_visited": ["Berlin", "Stuttgart"],
        "total_visits": [2]
    }
}
print(travel_logs_2["France"]["cities_visited"][1])
print(travel_logs_2["Germany"]["total_visits"][0])