import os
import cv2
from util import get_limits
from PIL import Image
"""
    Mắt người có 3 cơ quan cảm bien màu sac mỗi loại sẽ nhạy cảm với 1 loại bức sóng
    Cảm biến L
"""
webcam = cv2.VideoCapture(0)

yellow = [0, 255, 255] # yellow in BGR color space

while True:
    ret, frame = webcam.read()

    #Lý do chuyển sang HSV:
        #   +) giúp tách biệt tông màu ra khỏi độ sáng và độ bão hòa giúp dễ dàng phát hiện màu
        #   +) trong colorspace BGR thì giá trị máu sac thay đổi theo độ sáng và độ bão hòa
    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color = yellow)

    #Tạo mặt nạ là một ảnh đen-trang(nhị phân) trong đó pixel có màu nằm trong khoảng lower->upper được giu lại
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    #Chuyển mask thành đối tượng Image của PIL( để dùng phuong thức getbox() của PIL)(áp dụng với binaryImage)
    mask_ = Image.fromarray(mask)

    #tìm hình chữ nhật nhỏ nhất chứa pixel trắng
    bbox = mask_.getbbox()

    if bbox is not None:

        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)


    if ret:
        frame = cv2.resize(frame, (640, 480))
        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

webcam.release()
cv2.destroyAllWindows()


"""
    hay cho toi biet nhung thay doi nay tren git
"""




