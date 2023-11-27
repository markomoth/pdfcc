import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF
import minecart
import pdf2image
from pdf2image import convert_from_path
import numpy as np

def count_pages(pdf_path):
    doc = fitz.open(pdf_path)
    total_pages = doc.page_count
    
    colors=set()

    colored_pages = 0
    bw_pages = 0
    images = convert_from_path("test.pdf", 120, poppler_path = r"bin")
    
    for image in images:
        img = np.array(image.convert('HSV'))
        hsv_sum = img.sum(0).sum(0)
        if hsv_sum[0] == 0 and hsv_sum[1] == 0:
            bw_pages += 1
        else:
            colored_pages += 1

    doc.close()

    return total_pages, colored_pages, bw_pages

def load_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        total_pages, colored_pages, bw_pages = count_pages(file_path)
        result_label.config(
            text=f"Total Pages: {total_pages}\nColored Pages: {colored_pages}\nB&W Pages: {bw_pages}"
        )

# GUI setup
root = tk.Tk()
root.title("PDFcc")

load_button = tk.Button(root, text="Load PDF", command=load_pdf)
load_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
