import cv2
import sys
import math
import cv2 as cv
import numpy as np

def roi(img, vertices):

    #blank mask:
    mask = np.zeros_like(img)          # np.zeros = np array의 값을 0으로 초기화 하는 것 (1)

    #filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, 255)  # cv2.fillPoly = fillPoly : 오브젝트, 면을 생성한다.
                                       # mask : 마스크, vertices : 위에서 받아온 값, 255 : 영역을 정하는 것 (색)
                                       # 영역을 설정할 때 한개의 값만 쓰면 RGB 세개 다 똑같이 255로 설정한 것과 똑같다.

    #returning the image only where mask pixels are nonzero
    masked = cv2.bitwise_and(img, mask)     # and연산을 해서 겹치는 부분을 제외한 나머지는 날린다. (2)
    return masked

cap = cv2.VideoCapture(0)

while (True):
    ret, src = cap.read()

    src = cv2.resize(src, (640, 360))

    dst = cv.Canny(src, 50, 200, None, 3)

    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)

    vertices = np.array([[0,360],[0,240],[160,120], [480,120],[640,240],[640,320]], dtype=np.int32)
    # 리스트 안에 리스트는 2차원 배열이다. 튜플로 점을 정하고 있다.
    # 리스트를 만들어서 쓰면 그것을 지정한 것도 하나의 리스트여야 안의 리스트를 볼 수 있다.
    # 그래서 [veritces] 라고 리스트로 만들어줬다.

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