from PIL import Image

PNG_PATH = "sad.png"
ICO_PATH = "sad.ico"

# Open the PNG image
img = Image.open(PNG_PATH)

# Ensure image is RGBA (transparency in the png) A = Alpha
img = img.convert("RGBA")

# Save the image as a .ico !
img.save(ICO_PATH, format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])

print(f"Converted {PNG_PATH} to {ICO_PATH} successfully!")
