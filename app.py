import os, sys
from PIL import Image
from PIL import ImageFilter

im = Image.open("test.jpg")
low = Image.open("low-quality.jpg")
print(im.format, im.size, im.mode)
print(low.format, low.size, low.mode)
low.crop()

def transform_into_png():
  for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".png"
    if infile != outfile:
      try:
        with Image.open(infile) as im:
          im.save(outfile)
      except OSError:
        print("Cannot Convert: ", infile)
        

def img_enhancement():
  pass

def pfp_resizer():
  pass
