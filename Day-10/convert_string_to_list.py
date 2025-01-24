# Convert string to list
def main():
    folder_path = input("Enter the folder names seperated by spaces: ").split()
    print(folder_path)

    for folder in folder_path:
        print(folder)

if __name__ == "__main__":
    main()

