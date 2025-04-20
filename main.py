from tkinter import *
import os
try:
    import requests
except:
    os.system("pip3 install requests")

def scraper():
    # Form Values
    url_value = url_entry.get()
    tag_value = tag_entry.get()
    code = requests.get(url_value)
    try:
        f = open(tag_value,'w')
        f.write(code.text)
        print(tag_value + " file was created successfully")
    except:
        print("An error occoured \n")
    f.close()

wn = Tk()
wn.configure(bg='black')
wn.title("Web Scraper")
wn.geometry("500x500")

# Heading
heading = Label(
    wn,
    text="Web Scraper",
    font=("Helvetica", 32, "bold"),
    fg="white",
    bg="black"
)
heading.pack(pady=20)

# URL Label and Entry
url_label = Label(wn, text="Enter URL:", font=("Helvetica", 14), fg="white", bg="black")
url_label.pack()
url_entry = Entry(wn, width=50)
url_entry.pack(pady=10)

# Tag Label and Entry
tag_label = Label(wn, text="Enter File Name (eg: index.html):", font=("Helvetica", 14), fg="white", bg="black")
tag_label.pack()
tag_entry = Entry(wn, width=50)
tag_entry.pack(pady=10)

# Submit Button
submit_button = Button(wn, text="Submit", font=("Helvetica", 12), command=scraper)
submit_button.pack(pady=20)

# Run the app
wn.mainloop()
