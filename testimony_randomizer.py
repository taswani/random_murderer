import random

suspects = ["Varun Arora", "Vivek Loganathan", "David Ju", "Alexander Burns", "Guruprasad Ramprakash", "Anci Sun", "Anup Sonti", "Gary Wang", "Sara Hamilton", "Aiswarya Loganathan", "Andy Cheon", "Vivian Look", "Amber Loredo", "Tarun Sonti", "Grace Leu", "Michael Leu", "David Leu", "Andrew Burns"]
suspects2 = suspects.copy()
random.shuffle(suspects2)

file = open("text_files/testimonies.txt", "w")
file.write("Testimony Relations\n\n")
for index in range(len(suspects)):
    file.write(suspects[index] + " -> " + suspects2[index] + "\n")
file.close
