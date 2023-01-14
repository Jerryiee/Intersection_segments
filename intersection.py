import cv2
import numpy as np

def intersection(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if den == 0:
        return None

    xi = ((x3 - x4) * (x1 * y2 - y1 * x2) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
    yi = ((y3 - y4) * (x1 * y2 - y1 * x2) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den

    if (xi < min(x1, x2) or xi > max(x1, x2) or
        yi < min(y1, y2) or yi > max(y1, y2) or
        xi < min(x3, x4) or xi > max(x3, x4) or
        yi < min(y3, y4) or yi > max(y3, y4)):
        return None
    else:
        return (xi, yi)

import cv2

import cv2

import cv2

def draw_lines(img, lines):
    for line in lines:
        x1, y1, x2, y2 = line
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

def get_mouse_points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        param.append((x, y))

def main():
    img = np.zeros((512, 512, 3), np.uint8)
    line1_points = []
    line2_points = []

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', get_mouse_points, line1_points)

    while len(line1_points) < 2:
        cv2.imshow('image', img)
        cv2.waitKey(1)

    cv2.setMouseCallback('image', get_mouse_points, line2_points)

    while len(line2_points) < 2:
        cv2.imshow('image', img)
        cv2.waitKey(1)

    x1, y1 = line1_points[0]
    x2, y2 = line1_points[1]
    line1 = (x1, y1, x2, y2)

    x1, y1 = line2_points[0]
    x2, y2 = line2_points[1]
    line2 = (x1, y1, x2, y2)

    draw_lines(img, [line1, line2])
    intersection_point = intersection(line1, line2)

    if intersection_point:
        xi, yi = intersection_point
        cv2.circle(img, (int(xi), int(yi)), 5, (0, 255, 0), -1)
        cv2.putText(img, "Intersection point", (int(xi) + 10, int(yi)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    else:
        cv2.putText(img, "Lines do not intersect", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()