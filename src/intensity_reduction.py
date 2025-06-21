# src/intensity_reduction.py

import cv2
import numpy as np
import argparse
import os

def reduce_intensity(input_path, output_path, levels):
    # Load image as grayscale
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Cannot load image at {input_path}")

    # Validate levels: must be power of 2 between 2 and 256
    if levels < 2 or levels > 256 or (levels & (levels - 1)) != 0:
        raise ValueError("`levels` must be a power of 2 between 2 and 256")

    # Quantize: map [0,255] → [0, levels-1]
    q = np.floor(img.astype(np.float32) * levels / 256).astype(np.uint8)

    # Scale back to full 0–255 range
    out = (q * (255.0 / (levels - 1))).astype(np.uint8)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write result
    cv2.imwrite(output_path, out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Reduce an image’s gray levels to a specified power-of-2 count"
    )
    parser.add_argument(
        "input",
        help="Path to the input image (grayscale or color; will be converted to grayscale)"
    )
    parser.add_argument(
        "output",
        help="Path where the reduced-level image will be saved"
    )
    parser.add_argument(
        "--levels",
        type=int,
        default=2,
        help="Number of intensity levels (power of 2: 2, 4, 8, …, 256)"
    )
    args = parser.parse_args()

    reduce_intensity(args.input, args.output, args.levels)
