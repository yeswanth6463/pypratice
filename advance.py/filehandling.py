try:
    # Attempt to open the file "eng.txt" in read mode
    with open("eng1.txt", 'w') as fh:
        # Check if the file is readable
        if fh.readable():
            # Read and print the content of the file
            print(fh.read())
except FileNotFoundError as fe:
    # Handle the case where the file is not found
    print(fe)
