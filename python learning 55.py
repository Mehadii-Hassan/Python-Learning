txt_data = "I like pizza!"

file_path = "output.txt"

with open(file_path, "w") as file:
    file.write("I am Mehadi Hassan\n")
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")