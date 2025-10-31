from csv import writer
import os, csv

movie_file = "C:/Users/User/Desktop/Python Projects/MovieDB/movies.csv"
fields = ['title','year','director']


'''
Options
1. add new movie to list
2. list all movies in list
3. find movie by title
4. exit
'''

option = int(input("Please choose an option number.\n1. Add new Movie to list\n" \
    "2. List all movies in file\n3. Find movie by title\n4. Exit\nYour choice: ")
    )
    

if option == 1:
    movie = [str(movie) for movie in input("Enter Title, year and director seperate by a comma.\n").split(',')]
        
    with open(movie_file, 'a', newline='') as f:
        writer_obj = writer(f)
        writer_obj.writerow(movie)
    print("Successfully added your movie")


if option == 2:
    with open(movie_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)


if option == 3:
    search = input("Enter movie title: ")
    #comes back as string
    with open(movie_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if search.lower() == row["title"].lower():
                print(f"""title: {row['title']}, year: {row['year']}, director: {row['director']}""")
                     

if option == 4:
    exit(print('Exiting'))