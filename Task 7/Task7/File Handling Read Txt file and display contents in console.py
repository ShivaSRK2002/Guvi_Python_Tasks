def readFile(filename):  # Define function to read from text file
    f = open(filename, 'r')  # Open the file in read mode
    print(f.read())  # Print the contents of the file
    f.close()  # Close the file

filename = input("Enter file name: ")  # Enter the filename to be opened with .txt extension
readFile(filename)  # Call function with the input file name
