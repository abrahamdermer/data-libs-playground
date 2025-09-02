from PIL import Image, ImageDraw, ImageFont

# Create simple image
img = Image.new("RGB", (320, 200), "white")
draw = ImageDraw.Draw(img)
draw.rectangle((20,20,300,180), outline="black", width=3)
draw.text((30,30), "Hello PIL / שלום", fill="black")
img.save("image/pillow_out.png")
print("Saved image/pillow_out.png")
