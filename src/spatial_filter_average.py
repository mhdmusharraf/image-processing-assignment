# src/spatial_filter_average.py
import cv2, argparse, os

def spatial_avg(input_path, output_path, k):
    img = cv2.imread(input_path)
    if img is None:
        raise FileNotFoundError(f"Cannot load {input_path}")
    blurred = cv2.blur(img, (k, k))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, blurred)

if __name__=='__main__':
    p = argparse.ArgumentParser(description="Spatial average filter")
    p.add_argument("input",  help="Input image path")
    p.add_argument("output", help="Output image path")
    p.add_argument("--kernel", type=int, default=3, help="Kernel size")
    args = p.parse_args()
    spatial_avg(args.input, args.output, args.kernel)
