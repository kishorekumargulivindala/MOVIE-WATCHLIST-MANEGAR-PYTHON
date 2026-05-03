import json
import os

FILE_NAME = "movies.json"

# Load movies
def load_movies():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save movies
def save_movies(movies):
    with open(FILE_NAME, "w") as file:
        json.dump(movies, file, indent=4)

# Show movies
def show_movies(movies):
    if not movies:
        print("\nNo movies in your watchlist!")
        return

    print("\n🎬 Your Movie Watchlist:")
    for i, movie in enumerate(movies):
        status = "🍿 Watched" if movie["watched"] else "🎥 Not Watched"
        rating = f"⭐ {movie['rating']}/5" if movie["rating"] else "No Rating"
        print(f"{i+1}. {movie['name']} | {status} | {rating}")

# Main program
movies = load_movies()

while True:
    print("\n====== 🎬 MOVIE WATCHLIST ======")
    print("1. Add Movie")
    print("2. View Movies")
    print("3. Delete Movie")
    print("4. Mark as Watched")
    print("5. Rate Movie")
    print("6. Edit Movie")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Movie
    if choice == "1":
        name = input("Enter movie name: ")
        movies.append({"name": name, "watched": False, "rating": None})
        save_movies(movies)
        print("🎉 Movie added!")

    # View Movies
    elif choice == "2":
        show_movies(movies)

    # Delete Movie
    elif choice == "3":
        show_movies(movies)
        num = int(input("Enter movie number to delete: "))
        if 1 <= num <= len(movies):
            movies.pop(num - 1)
            save_movies(movies)
            print("🗑 Movie removed!")
        else:
            print("Invalid number!")

    # Mark as Watched
    elif choice == "4":
        show_movies(movies)
        num = int(input("Enter movie number: "))
        if 1 <= num <= len(movies):
            movies[num - 1]["watched"] = True
            save_movies(movies)
            print("🍿 Marked as watched!")
        else:
            print("Invalid number!")

    # Rate Movie
    elif choice == "5":
        show_movies(movies)
        num = int(input("Enter movie number: "))
        if 1 <= num <= len(movies):
            rating = int(input("Give rating (1-5): "))
            movies[num - 1]["rating"] = rating
            save_movies(movies)
            print("⭐ Rating added!")
        else:
            print("Invalid number!")

    # Edit Movie
    elif choice == "6":
        show_movies(movies)
        num = int(input("Enter movie number to edit: "))
        if 1 <= num <= len(movies):
            new_name = input("Enter new movie name: ")
            movies[num - 1]["name"] = new_name
            save_movies(movies)
            print("✏ Movie updated!")
        else:
            print("Invalid number!")

    # Exit
    elif choice == "7":
        print("🎬 Goodbye!")
        break

    else:
        print("Invalid choice!")