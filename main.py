import csv

MOVIE_FILE = "C:/Users/User/Desktop/Python Projects/MovieDB/movies.csv"
FIELDS = ['title', 'year', 'director']


def add_movie():
    """
    Adds a new movie to the CSV file after user inputs title, year, and director.
    """
    entry = input("Enter Title, Year, and Director separated by commas:\n")
    movie = [part.strip() for part in entry.split(',')]
    if len(movie) != len(FIELDS):
        print(f"Error: Please enter exactly {len(FIELDS)} values.")
        return
    with open(MOVIE_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(movie)
    print("Successfully added your movie.")


def list_movies():
    """
    Reads and prints all movies from the CSV file.
    """
    try:
        with open(MOVIE_FILE, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=FIELDS)
            print(f"{'Title':<30} {'Year':<6} {'Director'}")
            print("-" * 50)
            for row in reader:
                print(f"{row['title']:<30} {row['year']:<6} {row['director']}")
    except FileNotFoundError:
        print("No movies found; the movie database file does not exist.")


def find_movie():
    """
    Searches print movies matching the title entered by user (case-insensitive).
    """
    search = input("Enter movie title to search: ").strip().lower()
    with open(MOVIE_FILE, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=FIELDS)
        found = False
        for row in reader:
            if search == row['title'].strip().lower():
                print(f"Found: Title: {row['title']}, Year: {row['year']}, Director: {row['director']}")
                found = True
        if not found:
            print("No movie found with that title.")


def main():
    """
    Main menu loop for interacting with the movie database.
    """
    while True:
        print("\nOptions:\n1. Add new Movie\n2. List all Movies\n3. Find Movie by Title\n4. Exit")
        try:
            option = int(input("Your choice: ").strip())
        except ValueError:
            print("Invalid input. Enter a number between 1 and 4.")
            continue

        if option == 1:
            add_movie()
        elif option == 2:
            list_movies()
        elif option == 3:
            find_movie()
        elif option == 4:
            print("Exiting program.")
            break
        else:
            print("Please choose a valid option (1-4).")


if __name__ == "__main__":
    main()
