
![imagerecGIT](https://github.com/SiymX/ImageRecognizer/assets/63435885/a36ebe6a-1fd2-45ef-8af4-146ef8b822cc)

# ImageRecognizer
This is a Python-based Graphical User Interface (GUI) application for image recognition which uses a 
pre-trained ResNet-50 model. The application allows users to select an iamge file (JPG, JPEG, PNG, or GIF), and
it will predict the class of the image.





# Table of Contents
1. [Prequisites and Installation](#prequisites-and-installation)
2. [Features](#features)
3. [Usage](#usage)
4. [Compilation](#compilation)
5. [References](#references)







# Prequisites and Installation
Before running the application make sure you have the following dependencies installed:
- Python: (https://www.python.org/downloads/)
- tkinter package: `pip install tkinter`
- PIL package: `pip install pillow`
- torch package: `pip install torch`
- torchvision package: `pip install torchvision`







# Features
* **Image Classification**: The application uses the ResNet-50 model to classify the image and will provide the 
predicted class and confidence level. It has a powerful image recognition capabilities which was pre-trained on the
large-scale ImageNet dataset.
* **API Integration**: The program will fetch the class labels used for image classification from a JSON API endpoint.
It will retrieve the lables from the `imagenet-simple-lables` repository by [Anish Athayle](https://github.com/anishathalye). 
This makes sures that the predicted class names are accurate and up-to-date.
* **Preprocessing**: Before any classification, the application will apply preprocessing transformations to the image.
This includes resizing the selected image to a standard size of 224 x 224 pixels and then it will convert itself
to a Tensor format suitable for input to the ResNet-50 Model.
* **User-Friendly Interface**: The application provides a simple Graphical User Interface using the `tkinter` package.
Users can easily select and view images, and recieve immediate feedback on the predicted class and the confidence level.
* **Error Handling**: The application also handles various error scenarios, such as incorrect or invalid image
formats and files. It will let the user know the appropriate error message to guide the user in selecting the correct image
formats.








# Usage
1. Clone the repostory or download the source code file.
2. Open a terminal or command prompt and navigate to the project directory. You can also use the `exe` file to
test the application out from think link [here](https://www.dropbox.com/s/cp1ybvey75hiv01/ImageRecognition.exe?dl=0).
3. Run the following command to start the application:
```
python ImageRecognizer.py
```
4. The application window will appear and there you can click on the "Open Image" button to select an image to classify.
The supported formats include JPG, JPEG, PNG, and GIF.
5. The selected image will get displayed and also will analyze the image using the pre-trained ResNet-50 model and display the confidence level as well as the predicted class.







# Compilation
If you would like to distribute the application as an executable file, you can use [UPX](https://upx.github.io) and 
[Auto Py to Exe](https://pypi.org/project/auto-py-to-exe/) to compile the program. Extract the UPX archive to
a directory and then add the UPX directory to your system's PATH enviornment variable.


1. For terminal Install Auto Py to Exe Package:
```
pip install auto-py-to-exe
```
2. Run the following command to start the compilation process:
```
auto-py-to-exe
```
3. When the Auto Py to Exe GUI opens configure the options as per your requirements:
  * **Script Location** Select the `ImageRecognition.py` file.
  * **Onefile**: Select the checkbox to generate a single executable file.
  * **UPX**: Select the checkbox to compress the executable file using UPX (if UPX is installed and addted to PATH via advanced setting).
4. Click the `Convert .py to .exe` button to start the compilation process.
5. Once the compliation is finished, you can find the `exe` file in the output directory where it will be 
specified in.









# References
This is a pre-trained [ResNet-50 Model](https://datagen.tech/guides/computer-vision/resnet-50/) from the torchvision library.
The image classification labels used in this applications are from the `imagenet-simple-labels` repository by Anish Athalye.






