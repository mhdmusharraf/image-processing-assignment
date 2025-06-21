# src/rotate_image.py
import cv2, numpy as np, argparse, os

def rotate(input_path, output_path, angle):
    img = cv2.imread(input_path)
    if img is None:
        raise FileNotFoundError(f"Cannot load {input_path}")
    (h, w) = img.shape[:2]
    center = (w/2, h/2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    # compute new bounds
    cos, sin = np.abs(M[0,0]), np.abs(M[0,1])
    nw = int((h*sin) + (w*cos))
    nh = int((h*cos) + (w*sin))
    M[0,2] += (nw/2) - center[0]
    M[1,2] += (nh/2) - center[1]
    rotated = cv2.warpAffine(img, M, (nw, nh))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, rotated)

if __name__=='__main__':
    p = argparse.ArgumentParser(description="Rotate image")
    p.add_argument("input",  help="Input image path")
    p.add_argument("output", help="Rotated output path")
    p.add_argument("--angle", type=float, default=90,
                   help="Rotation angle in degrees")
    args = p.parse_args()
    rotate(args.input, args.output, args.angle)
