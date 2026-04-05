import numpy as np
import cv2

def pwlcm_map(x0, p, length):
    seq = np.zeros(length)
    seq[0] = x0
    for i in range(1, length):
        x = seq[i-1]
        if x < p:
            seq[i] = x / p
        elif x < 0.5:
            seq[i] = (x - p) / (0.5 - p)
        else:
            nx = 1 - x
            if nx < p:
                seq[i] = nx / p
            else:
                seq[i] = (nx - p) / (0.5 - p)
    return (seq >= np.mean(seq)).astype(int)

def extract_features(image_path, wm_shape):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    h -= h % 8
    w -= w % 8
    img = img[:h, :w]
    
    dc_matrix = np.zeros((h//8, w//8))
    for i in range(h//8):
        for j in range(w//8):
            block = img[i*8:(i+1)*8, j*8:(j+1)*8]
            dc_matrix[i, j] = np.mean(block)
            
    wm_h, wm_w = wm_shape
    bh = (h//8) // wm_h
    bw = (w//8) // wm_w
    
    sv_matrix = np.zeros((wm_h, wm_w))
    for i in range(wm_h):
        for j in range(wm_w):
            block = dc_matrix[i*bh:(i+1)*bh, j*bw:(j+1)*bw]
            sv_matrix[i, j] = np.linalg.norm(block, 2)
            
    return (sv_matrix >= np.mean(sv_matrix)).astype(int)

def embed_zero_watermark(image_path, watermark_path, x0=0.3, p=0.4):
    wm = cv2.imread(watermark_path, cv2.IMREAD_GRAYSCALE)
    _, wm_bin = cv2.threshold(wm, 127, 1, cv2.THRESH_BINARY)
    
    features = extract_features(image_path, wm_bin.shape)
    
    flat_wm = wm_bin.flatten()
    key_seq = pwlcm_map(x0, p, len(flat_wm))
    encrypted_wm = np.bitwise_xor(flat_wm.astype(int), key_seq)
    
    zero_wm = np.bitwise_xor(features.flatten().astype(int), encrypted_wm)
    return zero_wm, wm_bin.shape, key_seq

def extract_zero_watermark(attacked_image_path, zero_wm, wm_shape, key_seq):
    attacked_features = extract_features(attacked_image_path, wm_shape)
    
    encrypted_extracted = np.bitwise_xor(attacked_features.flatten().astype(int), zero_wm)
    decrypted_wm = np.bitwise_xor(encrypted_extracted, key_seq)
    
    return decrypted_wm.reshape(wm_shape)
