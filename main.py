import cv2 as cv
import sys


def read_and_show_image(img):
    img = cv.imread(cv.samples.findFile(img))
    cv.imshow("Display window", img)
    cv.waitKey(0)


def crop_image(img):
    img = cv.imread(cv.samples.findFile(img))
    height, width, channels = img.shape  # (1920, 1080, 3)
    cv.imshow("Display window", img)
    cv.imshow("Display window cropped", img[0:height // 2, 0:width // 2])  # y1:y2, x1:x2
    cv.imshow("Display window cropped2", img[height // 2:height, width // 2:width])  # y1:y2, x1:x2
    cv.waitKey(0)


def change_to_gray_image(img):
    img = cv.imread(cv.samples.findFile(img), cv.IMREAD_GRAYSCALE)  # в оперативной памяти
    # img2 = cv2.imread(path, cv2.IMREAD_COLOR)
    cv.imshow("Display window", img)
    cv.waitKey(0)


def change_to_bw_image(img):
    img = cv.imread(cv.samples.findFile(img), cv.IMREAD_GRAYSCALE)  # в оперативной памяти
    # img2 = cv2.imread(path, cv2.IMREAD_COLOR)
    # image_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # BGR(RGB) -> GRAY
    contrast = 90
    image = cv.threshold(img, contrast, 255, cv.THRESH_BINARY)[1]
    cv.imshow("Display window", image)
    cv.waitKey(0)


def change_quality_image(img):
    img = cv.imread(cv.samples.findFile(img), cv.IMREAD_COLOR)
    quality = 70
    cv.imwrite("src_avatar.jpg", img, [cv.IMWRITE_JPEG_QUALITY, quality])


def resize_image(img):
    img = cv.imread(cv.samples.findFile(img), cv.IMREAD_COLOR)
    height, width, channels = img.shape  # (1920, 1080, 3)
    multiply: float = 75 / 100  # 1.0 = 100%
    img2 = cv.resize(img, (int(width * multiply), int(height * multiply)))
    cv.imshow("Display img", img)
    cv.imshow("Display img2", img2)
    cv.waitKey(0)


if __name__ == '__main__':
    # read_and_show_image('woman.jpg')
    # crop_image('woman.jpg')
    # change_to_gray_image('woman.jpg')
    # change_to_bw_image('woman.jpg')
    # change_quality_image('woman.jpg')
    resize_image('woman.jpg')

    # data1 = [1, 2, 3, 4, 5, 6, 7, 9]
    # print(data1)
    # print(data1[:len(data1) // 2])
    pass
