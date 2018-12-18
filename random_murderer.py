import random

suspects = ["Varun Arora", "Vivek Loganathan", "David Ju", "Alexander Burns", "Guruprasad Ramprakash", "Anci Sun", "Anup Sonti", "Gary Wang", "Sara Hamilton", "Aiswarya Loganathan", "Andy Cheon", "Vivian Look", "Amber Loredo", "Tarun Sonti"]
roles = ["Lie Detector", "Rich Person", "Archaeologist", "Doctor", "Policeman", "Detective", "Doctor", "Copycat", "Lucky Gambler", "Master of Synergy", "Big Pharma Rep", "Marriage/Family Counselor", "Thief", "Businessman"]
rand_int = random.randint(0, 13)

file = open("text_files/murderer.txt", "w")
file.write("The murderer is {}!\n".format(suspects[rand_int]))
file.write("Their original role is {}.".format(roles[rand_int]))
file.close
