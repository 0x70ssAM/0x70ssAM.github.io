import sys
from PIL import Image

input_path = "assets/images/DevSecOps/Cloud-Native/devsecops-cloud-native.png"
output_path_jpg = "assets/images/DevSecOps/Cloud-Native/devsecops-cloud-native.jpg"
output_path_png = "assets/images/DevSecOps/Cloud-Native/devsecops-cloud-native.png"

img = Image.open(input_path).convert("RGB")
img = img.resize((1200, 630), Image.Resampling.LANCZOS)
img.save(output_path_jpg, "JPEG", quality=85)
# img.save(output_path_png, "PNG", optimize=True) # or just overwrite PNG if they want png?

print("Conversion complete!")
