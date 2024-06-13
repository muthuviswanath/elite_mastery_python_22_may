#Create a class called Photoshop. Create a method inside the class called as open
#The method should take any subclass of WindowsFile class as argument. 
# Create a class called WindowsFile and required subclasses like (JpegFile, PngFile, etc)

#WindowsFile class must have a method called as initializeProperties which is used to
#initialize the properties of the file.

#Each and every subclass of the WindowsFile class must contain its own implementation and
#methods

class Photoshop:
    def open(self, file_obj):
        print(f"File name is: {file_obj.filename}")
        print(f"File extension: {file_obj.extension}")
        print(f"File size: {file_obj.size}")
        if isinstance(file_obj ,JpegFile):
            file_obj.display()
        elif isinstance(file_obj,PngFile):
            file_obj.purpose()


class WindowsFile:
    filename = None
    extension = None
    size = None

    def initializeProperties(self,filename,extension,size):
        self.filename = filename
        self.extension = extension
        self.size = size

class JpegFile(WindowsFile):
    
    def display(self):
        print("Has million varieties of colors")


class PngFile(WindowsFile):
    def purpose(self):
        print("Used for Network Graphics")





ps = Photoshop()
jpeg = JpegFile()
jpeg.initializeProperties("MyPic","jpeg","128 KB")
png = PngFile()
png.initializeProperties("MyChildhoodPic","png","234 KB")
ps.open(jpeg)
print("--------------------------")
ps.open(png)