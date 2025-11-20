from notifypy import Notify
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk

title = ""
message = ""
icon = None
image_label = None

def select_image():
    global icon, image_label

    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=(("PNG files", "*.png"), ("JPG files", "*.jpg"), ("JPEG files", "*.jpeg"), ("All files", "*.*"))
    )
    if file_path:
        if image_label is not None:
            image_label.destroy()
            image_label = None
    
        pil_image = Image.open(file_path)
        ctk_image = ctk.CTkImage(light_image=pil_image, size=(64, 64))
        image_label = ctk.CTkLabel(app, image=ctk_image, text="ICON PREVIEW", text_color="white", compound="top")
        image_label.image = ctk_image
        image_label.pack(pady=10)
        icon = file_path

def sendNotification():
    notification = Notify()
    notification.title = textBox.get()
    notification.message = textBox2.get()
    if icon:
        notification.icon = icon
    notification.send()

app = ctk.CTk()
app.geometry("400x400")
app.title("Notification App")

textBox = ctk.CTkEntry(app, placeholder_text="Title of notification here", width=250)
textBox.pack(pady=20)

textBox2 = ctk.CTkEntry(app, placeholder_text="Message of notification here", width=250)
textBox2.pack(pady=20)

selectImageButton = ctk.CTkButton(app, text="Select Icon Image", command=lambda: select_image())
selectImageButton.pack(pady=10)

sendNotificationButton = ctk.CTkButton(app, text="Send Notification", command=lambda: sendNotification())
sendNotificationButton.pack(pady=20)

app.mainloop()