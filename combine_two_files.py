import sys

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
    if len(sys.argv) != 3:
            print("Usage: python script.py file1 file2")
            sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    result = max_difference(file1, file2)

    # Create a file for the output
    with open("output.txt", 'w') as f:
        f.write(str(result) + '\n')
