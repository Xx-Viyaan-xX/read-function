# opening the file in read mode
reading = open("codingal.txt", "r")
print(reading.readline())
reading.close()

writer = open("codingal.txt", "w")
writer.write("\nlodha, 12\n")
writer.close()

writer = open("codingal.txt", "a")
writer.write("\nishaan, 12\n")
writer.close()