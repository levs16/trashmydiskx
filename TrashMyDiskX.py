
########## ######  ####### ######  #   #   #      #
    ##     ##    # ##   ## #       #   #    #   #
    ##     ##    # ####### ######  # # #     # #
    ##     ######  ##   ##      #  #   #     #
    ##     ##    # ##   ## ######  #   #   #   #
###########################################     ###################################

# imports
import os, time

# how many files
times = int(input("?> How many files: "))

# what's the size
size_gb = float(input("?> File size (GB): ")) # original input is in bytes, so next thing is converting

# convert the input from size_gb to gb
size = int(size_gb * 1024**3)

# create a folder for storing those chunky bois
folder = "gigantic_files"

# handling the FileExistsError. Originally was handled with except, but became to complicated
if os.path.exists(folder):
    # if dir exists, we add the n to the folder name
    n = 1
    while os.path.exists(folder + f"_{n}"):
        n += 1
    folder = folder + f"_{n}"
    # use mkdir to create the folder
    os.mkdir(folder)
else:
    # else just create
    os.mkdir(folder)

# loop in range of the times input
for i in range(times):
    file_name = f"file_{i+1}.txt"
    file_path = os.path.join(folder, file_name)
    if os.path.exists(file_path):
        n = 1
        while os.path.exists(file_path + f"_{n}"):
            n += 1
        file_path = file_path + f"_{n}"
    with open(file_path, "wb") as f:
        f.write(os.urandom(size))
    print(f"log> File: {file_path}\nlog> Size:≈{size_gb}")

print(f"Done creating {times} files in {folder}")
