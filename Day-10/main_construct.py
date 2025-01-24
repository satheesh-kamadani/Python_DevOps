# Main construct

def main():
    folder_paths = input("Enter the folder paths seperated by space: ").split()
    print(folder_paths)

    for folder in folder_paths:
        print(folder)

if __name__ == "__main__":
    main()