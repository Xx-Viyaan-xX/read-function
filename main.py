reading = open("codingal.txt", "r")
print(reading.read())
reading.close()

reader = open("codingal.txt", "r")
print("\nReading in parts\n")
print(reader.read(3))
reader.close()

writer = open("codingal.txt", "a")
writer.write("viyaan, 12\n")
writer.close()



