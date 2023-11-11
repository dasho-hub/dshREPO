import sys

movie_count = int(input())
highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
rating_sum = 0
highest_rating_movie = ""
lowest_rating_movie = ""

for _ in range(movie_count):
    movie_name = input()
    movie_rating = float(input())
    rating_sum += movie_rating
    if movie_rating >= highest_rating:
        highest_rating = movie_rating
        highest_rating_movie = movie_name
    if movie_rating <= lowest_rating:
        lowest_rating = movie_rating
        lowest_rating_movie = movie_name

print(f"{highest_rating_movie} is with highest rating: {highest_rating :.1f}")
print(f"{lowest_rating_movie} is with lowest rating: {lowest_rating :.1f}")
print(f"Average rating: {rating_sum / movie_count :.1f}")
