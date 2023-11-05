books_checked = 0
target_book = input()
current_book = input()

while current_book != target_book:
    if current_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_checked} books.")
        break
    books_checked += 1
    current_book = input()

if current_book == target_book:
    print(f"You checked {books_checked} books and found it.")
