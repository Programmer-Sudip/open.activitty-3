# Program to remove lines starting with any prefix
file1 = open("Codingal", "r")
file2 = open("CodingalUpdated", "w")

# reading each line from original
# text file
for line in file1.readlines():
     # reading all lines that do not
     # begin with coding
    if not (line.startswith("coding")):

        # printing those lines
        print(line)
          
         # starting only those lines that
        # do not begin with coding
        file2.writelines(line)
 
# close and save the files
file1.close()
file2.close()


