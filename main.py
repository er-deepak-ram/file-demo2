# with keyword will manage the file directly and will close the file once we are done

with open("my_file.txt") as file:
    content = file.read()
    print(content)
    