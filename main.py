import cv2


image = cv2.imread('tc3.jpg')
watermark = cv2.imread('bossbaby.jpg')

print(watermark.shape)

x = image.shape[1] - watermark.shape[1]
y = image.shape[0] - watermark.shape[0]

watermark_place = image[y:, x:]
cv2.imwrite('bossbaby_place.jpg', watermark_place) 
print(watermark_place.shape)

blend = cv2.addWeighted(watermark_place, 0.5, watermark, 0.5, 0)
cv2.imwrite('nimona.jpg', blend)

image[y:, x:] = blend
cv2.imwrite('tc3-watermarked.jpg', image)