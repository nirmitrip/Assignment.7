def update_file(file="nirmit7.txt"):
    try:
        # Open the file in append mode
        f = open(file, "a")
        
        # Write data to the file
        roll_number = "30"
        name = "Nirmit Raut"
        class_name = "SYCO"
        f.writelines([roll_number + "\n", name + "\n", class_name + "\n"])
                
        # Reopen the file in read mode
        f = open(file, "r")
        
        # Read and print the data from the file
        print(f.readlines())

    except FileNotFoundError as err:
        print(f"Error: {err}")
    except IOError as err:
        print(f"Error: {err}")

# Call the function
update_file()