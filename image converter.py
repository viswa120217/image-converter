import os
from tkinter import Tk, Label, Button, OptionMenu, StringVar, filedialog
from PIL import Image, ImageTk

class SimpleImageConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter with Preview")
        self.root.geometry("300x400")

        self.label = Label(root, text="No image selected")
        self.label.pack(pady=10)

        self.preview_label = Label(root)
        self.preview_label.pack()

        Button(root, text="Upload Image", command=self.upload_image).pack(pady=5)

        self.selected_format = StringVar()
        self.selected_format.set("jpg")
        self.format_menu = OptionMenu(root, self.selected_format, "jpg", "png", "bmp", "gif", "webp")
        self.format_menu.pack(pady=10)

        Button(root, text="Convert", command=self.convert_image).pack(pady=5)

        self.image_path = None
        self.display_image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.webp")])
        if file_path:
            self.image_path = file_path
            filename = os.path.basename(file_path)
            self.label.config(text=f"Selected Image: {filename}")
            self.show_preview(file_path)

    def show_preview(self, path):
        try:
            img = Image.open(path)
            img.thumbnail((200, 200))
            self.display_image = ImageTk.PhotoImage(img)
            self.preview_label.config(image=self.display_image)
        except Exception as e:
            self.label.config(text="Error displaying image")

    def convert_image(self):
        if not self.image_path:
            self.label.config(text="No image selected")
            return

        save_format = self.selected_format.get()
        save_path = filedialog.asksaveasfilename(defaultextension=f".{save_format}",
                                                 filetypes=[(f"{save_format.upper()} files", f"*.{save_format}")])
        if save_path:
            try:
                img = Image.open(self.image_path)
                rgb_img = img.convert("RGB")
                rgb_img.save(save_path, save_format.upper())
                self.label.config(text=f"Image saved as {os.path.basename(save_path)}")
            except Exception as e:
                self.label.config(text="Conversion failed")

# ⚠️ Important: Call this only once per notebook session
root = Tk()
app = SimpleImageConverter(root)
root.mainloop()
