import tkinter as tk
from tkinter import messagebox, filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk, ImageOps
from rembg import remove
import io
import os

class RembgGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Remover (Drag & Drop)")
        self.root.geometry("600x500")

        # Canvas for image preview
        self.canvas = tk.Canvas(root, width=500, height=350, bg="gray")
        self.canvas.pack(pady=10)

        # Buttons
        self.btn_remove_bg = tk.Button(root, text="Remove Background", command=self.remove_bg, state=tk.DISABLED)
        self.btn_remove_bg.pack(pady=10)

        self.btn_save = tk.Button(root, text="Save Result", command=self.save_image, state=tk.DISABLED)
        self.btn_save.pack(pady=10)

        # Drag-and-drop area
        self.drop_label = tk.Label(root, text="Drag and drop an image here", bg="#ddd", relief="solid", width=50, height=2)
        self.drop_label.pack(pady=10)

        # Bind DnD event
        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind('<<Drop>>', self.drop_image)

        # Image storage
        self.original_image = None
        self.result_image = None
        self.display_image = None

    def drop_image(self, event):
        file_path = event.data.strip("{}")  # Handle paths with spaces
        if os.path.isfile(file_path):
            self.load_image(file_path)

    def load_image(self, filepath):
        try:
            self.original_image = Image.open(filepath).convert("RGBA")
            self.display(self.original_image)
            self.btn_remove_bg.config(state=tk.NORMAL)
            self.btn_save.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to open image:\n{e}")

    def remove_bg(self):
        if self.original_image is None:
            messagebox.showerror("Error", "No image selected!")
            return
        
        # Convert image to bytes for rembg
        img_bytes = io.BytesIO()
        self.original_image.save(img_bytes, format='PNG')
        result = remove(img_bytes.getvalue())
        self.result_image = Image.open(io.BytesIO(result)).convert("RGBA")
        
        self.display(self.result_image)
        self.btn_save.config(state=tk.NORMAL)

    def save_image(self):
        if self.result_image is None:
            return
        
        filepath = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")]
        )
        if filepath:
            # Save full resolution
            self.result_image.save(filepath)
            messagebox.showinfo("Saved", f"Image saved at:\n{filepath}")

    def display(self, img):
        # Scale only for preview (does not affect original image)
        preview = ImageOps.contain(img.copy(), (500, 350))
        self.display_image = ImageTk.PhotoImage(preview)
        self.canvas.delete("all")
        self.canvas.create_image(250, 175, image=self.display_image)

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = RembgGUI(root)
    root.mainloop()