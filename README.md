# Robust Zero-Watermarking Using Spatial Domain Features

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![NumPy](https://img.shields.io/badge/NumPy-Supported-orange)
![Institution](https://img.shields.io/badge/Institution-NITK-darkred)

## Overview
This repository contains a Python implementation of a **Digital Image Zero-Watermarking System** designed for copyright protection. Unlike traditional watermarking, this "zero-watermarking" approach extracts stable spatial-domain features from the host image, ensuring the original image remains completely undistorted (infinite PSNR).

The algorithm is specifically optimized for robustness against **Gaussian Noise** and **Image Blurring** by utilizing **DC coefficients** and **Matrix 2-norms** of $8 \times 8$ image blocks. Security is implemented via a **Piecewise Linear Chaotic Map (PWLCM)**, which encrypts the watermark before logical embedding.

## Key Features
* **Zero Distortion:** The host image pixels are mathematically untouched.
* **Spatial Feature Extraction:** Utilizes block-wise DC values and singular values (2-norms) for robust low-frequency representations.
* **PWLCM Encryption:** Secures the watermark payload against unauthorized extraction.
* **Targeted Robustness:** Specifically engineered to survive additive noise and smoothing/filtering attacks.

## Repository Structure
```text
frequency-domain-watermarking/
│
├── data/
│   ├── host_image.png          # Original cover image
│   ├── watermark_logo.png      # 32x32 binary watermark
│   ├── attack_noise.png        # Image after Gaussian Noise attack
│   ├── attack_blur.png         # Image after Median Blur attack
│   └── ...                     # Recovered watermark outputs
│
├── src/
│   ├── main.py                 # Feature extraction and key generation
│   ├── watermark.py            # Core logic for embedding, extraction, and PWLCM
│   └── test_robustness.py      # Automated attack simulation and NC evaluation
│
└── README.md
