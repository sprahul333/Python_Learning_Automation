# with statement in Python is used to provide a convenient syntax for working with objects
# that need to be set up and torn down in a specific way, such as files, locks, or database connections.
# It is designed to ensure that resources are properly acquired and released, even in the presence of exceptions or other control flow situations

from pathlib import Path

# mode = r+ --> Reading and writing
# mode = w+ ---> writing and reading (Overwrites the existing files or creates a new file)
# mode = a ---> Appending the data to the file ( adds the content to the existing files)
# mode = r ---> Reads the data from the file
# mode = w ---> Writes the data to the file (overwrites the existing data or creates a new file)
# Writing the data to the file

def write_data_to_file(data, file_path):
    """
    Writes the given data to the specified file path.

    Args:
        data (str): The data to be written to the file.
        file_path (str): The path to the file where the data should be written.
    """
    try:
        file_path = Path(file_path);

        if (file_path.exists() == False):
            with open(file_path, 'w') as file:
                file.write(data)
        else:
            with open(file_path, 'a') as file:
                file.write("\n" + data)

    except IOError as e:
        print(f"Error writing to file: {e}")


write_data_to_file("Contents", "Sample.txt")
write_data_to_file("New Data", "Sample.txt")

# Reads the data from the file
my_file = open("Sample.txt", "r")
print(my_file.read())

print("*******************************************************************************************")
print("Reading multiple lines of data at a time")

print("*******************************************************************************************")

my_file = open("Sample.txt", "r")
# Prints the list of lines present in the file
print(my_file.readlines())

my_file = open("Sample.txt", "r")
print("*******************************************************************************************")
print("Reading one line at a time")
print("*******************************************************************************************")
# Prints the first line present in the file
print(my_file.readline())

print("*******************************************************************************************")
my_file = open("Sample.txt", "r")
data=my_file.seek(0,5);
print(data)

# Closes the file object after all the operations are completed
my_file.close()

print("*******************************************************************************************")