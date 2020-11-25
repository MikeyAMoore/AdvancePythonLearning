file_builder = open("logger.txt", "w+")
for i in range(100):
  file_builder.write(f"I'm om line {i + 1}\n")
#file_builder.write("Hey, i'm in a file")

file_builder.close()