input_file = open("test.csv", "r+")
print (input_file.readlines())
input_file.close()

input_file = open("test.csv", "r+")
input_file.write("\nHeadset;50")
print(input_file.readlines())
input_file.close()

input_file = open("test.csv", "r+")
print(input_file.readlines())
input_file.close()
