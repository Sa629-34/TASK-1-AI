# Function to count the number of words in a file
def count_words(input_file, output_file):
    try:
        # Read the content of the input file
        with open(input_file, 'r') as file:
            content = file.read()

        # Count the words
        word_count = len(content.split())

        # Write the result to the output file
        with open(output_file, 'w') as file:
            file.write(f"The number of words in the file '{input_file}' is: {word_count}\n")

        print(f"Word count written to '{output_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input and output file names
input_file = input("Enter the name of the input text file: ")
output_file = input("Enter the name of the output text file: ")

# Count words and write the result
count_words(input_file, output_file)
