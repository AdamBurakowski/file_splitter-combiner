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


def combine_files(output_file, folder):
    with open(output_file, "wb") as output:
        part_number = 1
        while True:
            input_file = os.path.join(folder, f"part_{part_number:02d}.bin")
            if not os.path.exists(input_file):
                break
            with open(input_file, "rb") as p:
                output.write(p.read())
            part_number += 1


def main():
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
        combine_files(output, folder)
            
    else:
        print("You had one job...")

if __name__ == "__main__":
    main()
