# This program appends(adds) three additional names to philosophers.txt.
myfile = open("philosophers.txt", "a")
myfile.write("Matt\n")
myfile.write("Chris\n")
myfile.write("Suze\n")
myfile.close()