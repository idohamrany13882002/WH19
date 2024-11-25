oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman",
                 "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth",
                   "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

oscar_winners.add("Emma Watson")
print("a:", oscar_winners)  # to check

oscar_winners2 = oscar_winners.copy()
oscar_winners2.remove("Meryl Streep")
print("b:", oscar_winners2)  # to check
oscar_winners2.clear()
print("b:", oscar_winners2)  # to check

print("c:", dark_knight_actors & titanic_actors)  # to check

print("d:", iron_man_actors & avengers_actors)  # to check

print("e:", actor_list <= oscar_winners)  # to check

print("f:", avengers_actors <= actor_list)  # to check

print("g:", movie_cast.pop())  # to check

print("h:", movie_cast.remove("Matt Damon"))  # to check

print("i:", titanic_actors - oscar_winners)  # to check

print("j:", titanic_actors ^ dark_knight_actors)  # to check

oscar_winners.add("Cate Blanchard")
oscar_winners.add("Daniel Day Lewis")
print("k:", oscar_winners)  # to check

print("l:", titanic_actors | dark_knight_actors)  # to check
