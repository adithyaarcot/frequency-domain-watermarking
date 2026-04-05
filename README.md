# Robust Zero-Watermarking in Spatial Domain

This repository contains the implementation of a robust **Zero-Watermarking** scheme, based on the research paper: *"A Robust Zero-Watermarking Scheme in Spatial Domain by Achieving Features Similar to Frequency Domain"* (Ali & Kumar, 2024).

## 🚀 Overview
Traditional watermarking often sacrifices image quality (imperceptibility) to gain robustness. This project implements a **Zero-Watermarking** approach that protects copyright without altering a single pixel of the host image. By utilizing block-based DC values and matrix norms, this scheme achieves frequency-domain-level robustness while operating entirely in the spatial domain—making it significantly faster than DCT or SVD-based methods.

## 🛠 Features
*   **100% Imperceptibility:** The host image remains untouched; the watermark is "registered" rather than "embedded."
*   **Computational Efficiency:** Approximately **3x faster** than traditional DCT-SVD variants.
*   **PWLCM Security:** Uses a Piecewise Linear Chaotic Map to encrypt the watermark, ensuring only authorized users with the secret key can recover it.
*   **High Robustness:** Resilient against:
    *   Noise (Gaussian, Salt & Pepper, Speckle)
    *   Filtering (Average, Median, Gaussian Lowpass)
    *   JPEG Compression (Quality factors down to 20)
    *   Scaling and Cropping attacks.

## 📋 Algorithm Flow

### 1. Watermark Generation
1.  **Block Partitioning:** Divide the host image into $8 \times 8$ non-overlapping blocks.
2.  **DC Computation:** Calculate DC values in the spatial domain (average pixel intensity) without applying DCT.
3.  **Feature Extraction:** Further partition the DC matrix and use **Matrix 2-norm** to find maximum singular values.
4.  **Encryption:** Scramble the binary watermark using **PWLCM** with a secret initial value and control parameter.
5.  **XOR Construction:** Generate the final "Zero-Watermark" by XORing the binary feature matrix with the encrypted watermark.

### 2. Watermark Recovery
1.  Extract the feature matrix from the (potentially attacked) image using the same spatial-domain process.
2.  XOR the extracted features with the stored Zero-Watermark.
3.  Decrypt the result using the PWLCM secret keys to retrieve the original watermark.

## 💻 Getting Started

### Prerequisites
*   **MATLAB** (R2014b or newer) or **Python 3.x** (with NumPy and OpenCV).
*   Standard test images (Lena, Baboon, etc.) from the SIPI Image Database.

### Installation
```bash
git clone [https://github.com/adithyaarcot/your-repo-name.git](https://github.com/adithyaarcot/your-repo-name.git)
cd your-repo-name
