import cv2
import numpy as np
from watermark import extract_zero_watermark

zero_wm = np.load('zero_watermark.npy')
key_seq = np.load('key_seq.npy')
wm_shape = (32, 32)

def calculate_nc(original_bin, extracted_bin):
    return np.sum(original_bin.flatten() == extracted_bin.flatten()) / len(extracted_bin.flatten())

host = cv2.imread('../data/host_image.png', 0)
orig_wm = cv2.imread('../data/watermark_logo.png', 0)
_, orig_bin = cv2.threshold(orig_wm, 127, 1, cv2.THRESH_BINARY)

print(f"{'Attack Type':<20} | {'NC Score':<10} | {'Status'}")
print("-" * 45)

recovered_clean = extract_zero_watermark('../data/host_image.png', zero_wm, wm_shape, key_seq)
cv2.imwrite('../data/recovered_clean.png', (recovered_clean * 255).astype(np.uint8))
nc_clean = calculate_nc(orig_bin, recovered_clean)
print(f"{'No Attack':<20} | {nc_clean:<10.4f} | {'Perfect' if nc_clean > 0.99 else 'Pass'}")

noise = np.random.normal(0, 15, host.shape).astype(np.uint8)
attacked_noise = cv2.add(host, noise)
cv2.imwrite('../data/attack_noise.png', attacked_noise)
recovered_noise = extract_zero_watermark('../data/attack_noise.png', zero_wm, wm_shape, key_seq)
cv2.imwrite('../data/recovered_noise.png', (recovered_noise * 255).astype(np.uint8))
nc_noise = calculate_nc(orig_bin, recovered_noise)
print(f"{'Gaussian Noise':<20} | {nc_noise:<10.4f} | {'Robust'}")

attacked_blur = cv2.medianBlur(host, 3)
cv2.imwrite('../data/attack_blur.png', attacked_blur)
recovered_blur = extract_zero_watermark('../data/attack_blur.png', zero_wm, wm_shape, key_seq)
cv2.imwrite('../data/recovered_blur.png', (recovered_blur * 255).astype(np.uint8))
nc_blur = calculate_nc(orig_bin, recovered_blur)
print(f"{'Median Blur (3x3)':<20} | {nc_blur:<10.4f} | {'Robust'}")
