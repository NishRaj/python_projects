from PIL import Image, ImageDraw, ImageFont
img = Image.open(r'/home/nishank/Documents/ImpDocs/PassPortSizePhoto.jpg')
draw = ImageDraw.Draw(img)
text = 'NR'
font = font = ImageFont.load_default()
textwidth, textheight = draw.textsize(text,font)
width, height = img.size
x = width/2 - textwidth/2
y = height - textheight -50
draw.text((x,y), text, font=font)
img.save(r'passport.png')
Image.open('passport.png')

