#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting a List inside List but it is not that useful
["A", "B", ["C", "D"]]

#Nesting Dictionary in a Dictionary
travel = {
  "France": {"cities_visited": ["Paris" "Lille", "Dijon"], "times_visited": 12},

  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
  }

  #Nesting Dictionary in a List

travel = [
  {"Country": "France",
  "cities_visited": ["Paris" "Lille", "Dijon"],
  "times_visited": 12
  },
  {"Country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
  "total_visits": 5
  }
]