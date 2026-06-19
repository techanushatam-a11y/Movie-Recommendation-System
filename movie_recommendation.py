movies= {
    "Comedy": ["3 Idiots", "PK", "Chhichhore"],
    "Action": ["War", "Pathaan", "Krrish"],
    "Drama": ["Taare Zameen Par", "Dangal", "Super 30"]
}

genre = input("Enter genre (Comedy/Action/Drama): ")

if genre in movies:
    print("\nRecommended Movies:")
    for movie in movies[genre]:
        print(movie)
else:
    print("Genre not found!")
