import cv2
import numpy as np
from watermark import embed_zero_watermark, extract_zero_watermark

host_img = '../data/host_image.png'
wm_img = '../data/watermark_logo.png'

zero_watermark, shape, key = embed_zero_watermark(host_img, wm_img)

np.save('zero_watermark.npy', zero_watermark)

extracted_flat = extract_zero_watermark(host_img, zero_watermark, shape, key)
extracted_img = (extracted_flat * 255).astype(np.uint8)

cv2.imwrite('../data/extracted_watermark.png', extracted_img)

original_wm = cv2.imread(wm_img, cv2.IMREAD_GRAYSCALE)
_, orig_bin = cv2.threshold(original_wm, 127, 1, cv2.THRESH_BINARY)
nc = np.sum(orig_bin.flatten() == extracted_flat.flatten()) / len(extracted_flat)
print(f"Normalized Correlation (NC): {nc}")
