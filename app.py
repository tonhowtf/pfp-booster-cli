import os, sys
from PIL import Image, ImageOps
from PIL import ImageFilter
#test
sizes = {'discord':'128x128',
         'bluesky': '400x400',
         'telegram': '512x512',
         'twitter': '400x400',
         'whatsapp': '192x192'}


im = Image.open("test.jpg")
low = Image.open("low-quality.jpg")
# print(im.format, im.size, im.mode)
# print(low.format, low.size, low.mode)
print(os.path.basename())

def transform_into_png():
  for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".png"
    if infile != outfile:
      try:
        with Image.open(infile) as im:
          im.save(outfile)
          return outfile
      except OSError:
        print("Não foi possivel converter: ", infile)
  return None

def pfp_resizer():
  outfile = transform_into_png()
  if outfile is None:
    print('Nenhuma imagem encontrada.')
    return 0
  with Image.open(outfile) as im:
    base_name = os.path.splitext(os.path.basename(outfile))
    for platform, size_str in sizes.items():
      try:
        width, height = map(int, size_str.split('x'))
      except ValueError:
        print(f"{platform}: {size_str}")


