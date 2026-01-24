import tkinter as tk
from PIL import Image, ImageTk

# Create main window
root = tk.Tk()
root.title("Image in Tkinter")
root.geometry("400x400")

# Open image using PIL
upload = Image.open("Star.jpg")

# Convert image to Tkinter compatible format
image = ImageTk.PhotoImage(upload)

# Add image to Tkinter Label
label = tk.Label(root, image=image, height=350, width=300)
label.place(x=50, y=0)

# Add text below the image
label2 = tk.Label(
    root,
    text="This is how you add image in Tkinter Window"
)
label2.place(x=40, y=360)

# Run the application
root.mainloop()
