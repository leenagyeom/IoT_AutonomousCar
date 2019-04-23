import cv2
import sys
import math
import cv2 as cv
import numpy as np

def roi(img, vertices):

    #blank mask:
    mask = np.zeros_like(img)          # np.zeros = np array�� ���� 0���� �ʱ�ȭ �ϴ� �� (1)

    #filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, 255)  # cv2.fillPoly = fillPoly : ������Ʈ, ���� �����Ѵ�.
                                       # mask : ����ũ, vertices : ������ �޾ƿ� ��, 255 : ������ ���ϴ� �� (��)
                                       # ������ ������ �� �Ѱ��� ���� ���� RGB ���� �� �Ȱ��� 255�� ������ �Ͱ� �Ȱ���.

    #returning the image only where mask pixels are nonzero
    masked = cv2.bitwise_and(img, mask)     # and������ �ؼ� ��ġ�� �κ��� ������ �������� ������. (2)
    return masked

cap = cv2.VideoCapture(0)

while (True):
    ret, src = cap.read()

    src = cv2.resize(src, (640, 360))

    dst = cv.Canny(src, 50, 200, None, 3)

    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)

    vertices = np.array([[0,360],[0,240],[160,120], [480,120],[640,240],[640,320]], dtype=np.int32)
    # ����Ʈ �ȿ� ����Ʈ�� 2���� �迭�̴�. Ʃ�÷� ���� ���ϰ� �ִ�.
    # ����Ʈ�� ���� ���� �װ��� ������ �͵� �ϳ��� ����Ʈ���� ���� ����Ʈ�� �� �� �ִ�.
    # �׷��� [veritces] ��� ����Ʈ�� ��������.

    Roi_img = roi(dst, [vertices])

    cdstP = np.copy(Roi_img)

    lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            cv.line(cdst, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)

    linesP = cv.HoughLinesP(cdstP, 1, np.pi / 180, 50, None, 50, 10)

    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv.LINE_AA)

    cv.imshow("Source", src)
    cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()