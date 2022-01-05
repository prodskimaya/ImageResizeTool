# ImageResize Tool
Tool made for the FWA Yearbook Team to resize multiple images quickly. Make sure to check this repo for future updates

## How to Use
There are multiple ways to use the ImageResize Tool. If you don't use the tool much, use the **Drag & Drop Method**. However, if you need to use the program frequently then I recommend the **Advanced Method**. The Advanced Method allows you to quickly access the program in the future (In the **Open With** tab)

### Method 1: Drag & Drop
1. Download and extract the tool
2. Drag Images onto **ImageResize.exe** to resize them

### Method 2: Advanced Method
1. Download and extract the tool
2. Right click on the image(s) you want to resize
3. Click **Properties** and then click **Change**
4. Scroll down and click **Look for other app on PC**
5. Find and Select **ImageResize.exe**

## Program not Working?
Does the program not function correctly or is an error is printed in the console? Please open an **Issue Card** so we can fix it ASAP!

## Stuff for Nerds
The ImageResize Tool was written in Python 3.8 using Pycharm by Jetbrains.
PyInstaller is used to convert the tool to an .exe file

### ImageResize Python requirements
1. Python 3.8 or later
2. Pillow `pip install Pillow`
3. PyInstaller `pip install pyinstaller`

### How to Build ImageResize
1. Run this command:
```
  pyinstaller --onefile ImageResize.py
```
2. Zip-up the **dist** folder
3. Distribute!
