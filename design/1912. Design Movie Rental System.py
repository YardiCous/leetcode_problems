# You have a movie renting company consisting of n shops. You want to implement a renting system that supports searching for, booking, and returning movies. The system should also support generating a report of the currently rented movies.
#
# Each movie is given as a 2D integer array entries where entries[i] = [shopi, moviei, pricei] indicates that there is a copy of movie moviei at shop shopi with a rental price of pricei. Each shop carries at most one copy of a movie moviei.
#
# The system should support the following functions:
#
#     Search: Finds the cheapest 5 shops that have an unrented copy of a given movie. The shops should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopi should appear first. If there are less than 5 matching shops, then all of them should be returned. If no shop has an unrented copy, then an empty list should be returned.
#     Rent: Rents an unrented copy of a given movie from a given shop.
#     Drop: Drops off a previously rented copy of a given movie at a given shop.
#     Report: Returns the cheapest 5 rented movies (possibly of the same movie ID) as a 2D list res where res[j] = [shopj, moviej] describes that the jth cheapest rented movie moviej was rented from the shop shopj. The movies in res should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopj should appear first, and if there is still tie, the one with the smaller moviej should appear first. If there are fewer than 5 rented movies, then all of them should be returned. If no movies are currently being rented, then an empty list should be returned.
#
# Implement the MovieRentingSystem class:
#
#     MovieRentingSystem(int n, int[][] entries) Initializes the MovieRentingSystem object with n shops and the movies in entries.
#     List<Integer> search(int movie) Returns a list of shops that have an unrented copy of the given movie as described above.
#     void rent(int shop, int movie) Rents the given movie from the given shop.
#     void drop(int shop, int movie) Drops off a previously rented movie at the given shop.
#     List<List<Integer>> report() Returns a list of cheapest rented movies as described above.
#
# Note: The test cases will be generated such that rent will only be called if the shop has an unrented copy of the movie, and drop will only be called if the shop had previously rented out the movie.

# Solution
# Usage of SortedList, SortedList is really good for lazy heap as you can remove stuff by specifying it unlike heaps, meaning you can give a certain type in 
# the SortedList like (1,"2",False) and it will be able to remove it for you.
# TC: search: O(1)
# TC: rent: O(log N)
# TC: drop: O(log N)
# TC: report: O(1)

# SC: O(N)

from typing import List
from collections import defaultdict

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = defaultdict(SortedList)
        self.prices = defaultdict(int)
        self.rent_movies = SortedList()
        for shop,movie,price in entries:
            self.movies[movie].add((price,shop))
            self.prices[(shop,movie)] = price
    def search(self, movie: int) -> List[int]:
        return [shop for _,shop in self.movies[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        self.movies[movie].remove((self.prices[(shop,movie)],shop))
        self.rent_movies.add((self.prices[(shop,movie)],shop,movie))

    def drop(self, shop: int, movie: int) -> None:
        self.movies[movie].add((self.prices[(shop,movie)],shop))
        self.rent_movies.remove((self.prices[(shop,movie)],shop,movie))
    def report(self) -> List[List[int]]:
        return [[shop,movie] for _,shop,movie in self.rent_movies[:5]]



# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
