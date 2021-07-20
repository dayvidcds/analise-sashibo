import cv2
import convert

# Import picture & create HSI copy using algorithm
img = cv2.imread('img.jpg', 1)
img = cv2.resize(img, (400, 300))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hsi = convert.RGB_TO_HSI(img)

# Display HSV Image
cv2.imshow('HSI Image', hsi)

# The three value channels
cv2.imshow('H Channel', hsi[:, :, 0])
cv2.imshow('S Channel', hsi[:, :, 1])
cv2.imshow('I Channel', hsi[:, :, 2])

values = [hsi[:, :, 0].mean(), hsi[:, :, 1].mean(), hsi[:, :, 2].mean()]

print(values)

cv2.imshow('HSV', hsv)

# Wait for a key press and then terminate the program
cv2.waitKey(0)
cv2.destroyAllWindows()