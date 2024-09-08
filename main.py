from tkinter import *
from tkinter import PhotoImage
import os

# Initialize global variables
last_x = 0
button_number = 0
y = 10

# Get the current file's path and directory
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)

# Define the subfolder where the book covers and PDFs are stored
book_cover_dir = os.path.join(current_dir, 'book cover')
pdf_books_dir = os.path.join(current_dir, 'pdf books')

# Define the path to the icon file
icon_path = os.path.join(current_dir, 'icon.ico')

def open_pdf(pdf_path):
    """Function to open the PDF file when the button is clicked."""
    if os.path.exists(pdf_path):
        os.startfile(pdf_path)  # This works on Windows
    else:
        print(f"Error: The file {pdf_path} does not exist.")

def make_bu(root, cover_path, book_name, pdf_path, images_list):
    global last_x
    global y
    global button_number

    # Check if the image file exists
    if not os.path.exists(cover_path):
        print(f"Error: The file {cover_path} does not exist.")
        return

    # Load the image and resize it
    cover = PhotoImage(file=cover_path).subsample(3)

    # Create buttons for books with the images
    if button_number == 4:
        last_x = 0
        y = 300
        b = Button(root, text=book_name, image=cover, compound="top", bg="#000000",
                   font=("arial", 15, "bold"), width=100, height=200, pady=10, fg="#FFFFFF",command=lambda: open_pdf(pdf_path))
        b.place(x=last_x + 20, y=y)
        last_x = last_x + 290
        button_number += 1
    else:
        b = Button(root, text=book_name, image=cover, compound="top", bg="#000000",
                   font=("arial", 10, "bold"), width=100, height=200, pady=10,  fg="#FFFFFF",command=lambda: open_pdf(pdf_path))
        b.place(x=last_x + 20, y=y)
        last_x = last_x + 290
        button_number += 1

    # Store a reference to prevent garbage collection
    images_list.append(cover)

# Initialize the Tkinter root window
root = Tk()
root.title("A Mini Book Library")
root.geometry("1024x700+250+50")
root.resizable(0, 0)
root.configure(background="#FFFFFF")

# Set the window icon
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
else:
    print(f"Error: The icon file {icon_path} does not exist.")

# List to hold image references
images_list = []

# Create paths to the image files and corresponding PDF files, and call the make_bu function for each book
for i in range(1, 9):
    photo_path = os.path.join(book_cover_dir, f"book {i}.png")
    pdf_path = os.path.join(pdf_books_dir, f"book {i}.pdf")
    book_name = ["عجائب الكون", "السماء + الارض", "الفضاء والزمن", "رحلة في الفضاء", "مقدمة عن الفلك", "الكون والثقب الأسود","ميكانيكا السيارات","الصيانه الذاتيه في ويندوز"][i - 1]
    make_bu(root, photo_path, book_name, pdf_path, images_list)

exit_b = Button(root, text = "EXIT",bg = "#00ff00",font=("arial",25,"bold"),command=lambda:exit())
exit_b.pack(side="bottom",pady=  25)
print("Done!")
# Start the Tkinter event loop
root.mainloop()