from PIL import Image
import os
image_file = "out.png"
img_org = Image.open(image_file)
width_org, height_org = img_org.size
factor = 2
width = int(width_org * factor)
height = int(height_org * factor)
img_anti = img_org.resize((width, height), Image.ANTIALIAS)
name, ext = os.path.splitext(image_file)

new_image_file = "out_zoomed%s" % (ext)
img_anti.save(new_image_file)
print("resized file saved as %s" % new_image_file)

#import webbrowser
#webbrowser.open(new_image_file)
