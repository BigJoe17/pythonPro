def main():

   
    booklist = []
    choice = 0 
    while choice != 4:
        print("\n")
        print("*** Books Manager ***")
        print("1. Add Book ")
        print("2. look up a book  ")
        print("3. Display books ")
        print("4. Quit ")
        try:
                choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            print("adding Book...")
            nbook = input("enter book name:\t")
            nAuthor = input("enter the author of Book:\t")
            nPages = input("Enter the no of Pages:\t")

            booklist.append({"name":nbook, "author":nAuthor, "pages":nPages})
            print(f"Book {nbook} by {nAuthor} added succesfully... ")

        elif choice == 2:
            print("looking up a Book...")
            keyword = input("enter search term(name or author):")
            found = False

            for book in booklist:
                if keyword in book["name"].lower() or keyword in book["author"].lower():
                    print(f"Found:{book}")
                    found = True
            if not found:
                print("No books found matching the search term.")
            
        elif choice == 3:
            print("Displaying Book..")
            for i in range(len(booklist)):
                print(booklist[i])

        elif choice == 4:
            print("Quitting Program")
        print("Program Terminated")
        


if __name__ == "__main__":
    main()