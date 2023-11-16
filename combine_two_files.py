import sys
import os

def max_difference(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            list_f1 = [float(line.strip()) for line in f1]
            list_f2 = [float(line.strip()) for line in f2]

        max1 = max(list_f1)
        max2 = max(list_f2)

        return abs(max2 - max1)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py file1 file2 output_folder")
        sys.exit(1)
    output_folder = sys.argv[1]
    file1 = sys.argv[2]
    file2 = sys.argv[3]

    result = max_difference(file1, file2)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Create a file for the output in the specified folder
    with open(output_folder, 'w') as f:
        f.write(str(result) + '\n')
    
