# src/block_average.py
import cv2, numpy as np, argparse, os

def block_avg(input_path, output_path, bsize):
    img = cv2.imread(input_path)
    if img is None:
        raise FileNotFoundError(f"Cannot load {input_path}")
    h, w = img.shape[:2]
    out = img.copy()
    for y in range(0, h, bsize):
        for x in range(0, w, bsize):
            block = img[y:y+bsize, x:x+bsize]
            avg = block.mean(axis=(0,1)).astype(np.uint8)
            out[y:y+bsize, x:x+bsize] = avg
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, out)

if __name__=='__main__':
    p = argparse.ArgumentParser(description="Block-wise averaging")
    p.add_argument("input",  help="Input image path")
    p.add_argument("output", help="Output image path")
    p.add_argument("--block", type=int, default=3, help="Block size")
    args = p.parse_args()
    block_avg(args.input, args.output, args.block)
