import tkinter as tk
import PIL
import torch
import urllib.request
import json
from tkinter import filedialog
from PIL import Image, ImageTk
from torchvision import models, transforms
from torchvision.models.resnet import ResNet50_Weights

model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
model.eval()

preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

class_labels_url = 'https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json'
response = urllib.request.urlopen(class_labels_url)
class_labels = json.load(response)

window = tk.Tk()
window.title("Image Recognition")
window.geometry("900x900")


def create_gradient(width, height):
    base = Image.new('RGB', (width, height), '#2C3E50')
    top = Image.new('RGB', (width, height), '#4CA1AF')
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend(list(int(255 * (x / width)) for x in range(width)))
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base


def open_image():
    file_path = filedialog.askopenfilename(initialdir='/', title='Select an Image',
                                           filetypes=[('Image Files', ('*.jpg', '*.jpeg', '*.png', '*.gif'))])
    if file_path:
        error_label.config(text="")

        try:
            panel.configure(image=None)
            panel.image = None
            result_label.config(text="")
            confidence_label.config(text="")

            image = Image.open(file_path)

            if image.mode == 'RGBA':
                image = image.convert('RGB')

            image = image.resize((600, 600))

            photo = ImageTk.PhotoImage(image)

            panel.configure(image=photo)
            panel.image = photo

            img = preprocess(image)
            img = torch.unsqueeze(img, 0)

            with torch.no_grad():
                output = model(img)

            _, predicted_idx = torch.max(output, 1)
            predicted_class = class_labels[predicted_idx]
            confidence = torch.softmax(output, 1)[0][predicted_idx] * 100

            result_label.config(text="Predicted class: " + predicted_class)
            confidence_label.config(text="Confidence: " + str(round(confidence.item(), 2)) + "%")
        except (OSError, PIL.UnidentifiedImageError):
            panel.configure(image=None)
            panel.image = None
            result_label.config(text="")
            confidence_label.config(text="")
            error_label.config(text="Incorrect format. Please upload one of the following formats: JPG, JPEG, PNG, GIF")


gradient = create_gradient(900, 900)
background_image = ImageTk.PhotoImage(gradient)
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(window, text="Image Recognition", font=("Arial", 24))
label.pack(pady=10)

open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack(pady=10)

panel = tk.Label(window)
panel.pack()

result_label = tk.Label(window, text="")
result_label.pack()
confidence_label = tk.Label(window, text="")
confidence_label.pack()

error_label = tk.Label(window, text="", fg="red")
error_label.pack()

footer_label_font = ('Arial', 10)
footer_label = tk.Label(window, text="Copyright © Khandakar Sayeem. All Rights Reserved. 2023", font=footer_label_font)
footer_label.pack(side=tk.BOTTOM, pady=10)

window.mainloop()
