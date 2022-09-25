# number of moviews released in 2022

fmovies=open("movies.txt")
all_movies=[]
for line in fmovies:
    movies=line.rstrip("\n").split(",")
    all_movies.append(movies)
# print(all_movies)

count=0
for mov in all_movies:
    if mov[1]=="2022":
        count+=1
print(count)


# number malayalam movies

malayalam_mov=[mov for mov in all_movies if mov[-2]=="malayalam"]
print(malayalam_mov)


# theater released movies

theater_release=[mov for mov in all_movies if mov[-1]=="theater"]
print(theater_release)

# list of movies whose rating > 5

rating5=[mov for mov in all_movies if mov[2]>"5"]
print(rating5)

# {released movies->2022:4,2021:6,2020:2}

year_released={}
mov_year=[mov[1] for mov in all_movies]
print(mov_year)
for mov in mov_year:
    if mov in year_released:
        year_released[mov]+=1
    else:
        year_released[mov]=1
print(year_released)


# highest movie release year=2021

print(max(year_released, key=lambda mov : year_released[mov]))

