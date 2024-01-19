import os

print("do you want to split file into smaller chunks, or combine chunks into original file?")
action = input("type s to split or c to combine: ")

def split_file(input_file, chunk_size):
    with open(input_file, "rb") as f:
        chunk = f.read(chunk_size)
        part_number = 1

        while chunk:
            output_file = f"part_{part_number:02d}.bin"
            with open(output_file, "wb") as part:
                part.write(chunk)
            part_number += 1
            chunk = f.read(chunk_size)


def combine_files(output_file, *input_files):
    with open(output_file, "wb") as output:
        for input_file in input_files:
            with open(input_file, "rb") as part:
                output.write(part.read())


if action == "s":
    size = int(input("type the size of an output chunk (in KB): "))
    file = input("type the  path of the file you wish to split up: ")
    split_file(file, size * 1024)
elif action == "c":
    output = input("type path of the file you want to create: ")
    folder = input("type the path of the folder in which you store the chunks\n(if you don't store them in the same folder do so): ")
    if not os.path.exists(folder):
        print("Error: The specified folder path does not exist.")
        exit()
    print("type names of all chunks of a file you wish to restore (to finish type end): ")
    chunk_number = 1
    chunks = []
    while True:
        chunk = input(f"chunk number {chunk_number}: ")
        if chunk == "end":
            break
        chunks.append(os.path.join(folder, chunk))
        chunk_number += 1
    combine_files(output, *chunks)
        
else:
    print("You had one job...")
