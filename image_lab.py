import cv2
import os

# ------------------ Load Image ------------------
img = cv2.imread("Assignment_Image.jpg")

if img is None:
    print("Image not found! Put Assignment_Image.jpg in the same folder.")
    exit()
else:
    print(" Image Loaded Successfully!")

# Create output folder in same directory
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

def save(name, image):
    cv2.imwrite(os.path.join(output_folder, name), image)

# ------------------ Grayscale ------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
save("gray.jpg", gray)

# ------------------ Resize ------------------
h, w = img.shape[:2]
new_w = 400
new_h = int((new_w / w) * h)
resized = cv2.resize(img, (new_w, new_h))
save("resized.jpg", resized)

# ------------------ Gaussian Blur ------------------
blur3 = cv2.GaussianBlur(img, (3,3), 0)
blur5 = cv2.GaussianBlur(img, (5,5), 0)
blur7 = cv2.GaussianBlur(img, (7,7), 0)
save("blur3.jpg", blur3)
save("blur5.jpg", blur5)
save("blur7.jpg", blur7)

# ------------------ Canny Edge Detection ------------------
edges_low = cv2.Canny(gray, 50, 100)
edges_mid = cv2.Canny(gray, 100, 200)
edges_high = cv2.Canny(gray, 150, 250)
save("edges_low.jpg", edges_low)
save("edges_mid.jpg", edges_mid)
save("edges_high.jpg", edges_high)

# ------------------ Drawing Shapes ------------------
draw = img.copy()
cv2.rectangle(draw, (50,50), (200,200), (0,0,255), 2)
cv2.rectangle(draw, (250,50), (450,250), (0,0,255), 5)
cv2.circle(draw, (150,350), 50, (0,255,0), 2)
cv2.circle(draw, (400,350), 80, (0,255,0), 5)
save("shapes.jpg", draw)

# ------------------ Gray Level Slicing ------------------
low, high = 100, 200
slice_with_bg = gray.copy()
slice_with_bg[(gray < low) | (gray > high)] = 0

slice_without_bg = gray.copy()
slice_without_bg[(gray >= low) & (gray <= high)] = 255
slice_without_bg[(gray < low) | (gray > high)] = 0

save("slice_with_bg.jpg", slice_with_bg)
save("slice_no_bg.jpg", slice_without_bg)

# Save original too
save("original.jpg", img)

print("\n ALL IMAGES SAVED SUCCESSFULLY in 'output' folder!")
