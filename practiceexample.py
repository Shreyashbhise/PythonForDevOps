for i in range(1,3):
    file_name = "file{}.txt".format(i)

    with open(file_name,'w') as file:
        pass

print(" 2 file created successfully")