import numpy as np
import  argparse
import imutils
import cv2
import answer_sheet1.test9 as bian

# 正确答案
# ANSEER_KEY = {0:1,1:1,2:1,3:3 }
# 通过闭操作(先膨胀,再腐蚀)将数字连在一起
# rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(9 ,3))
def order_points(pts):
    # 一共四个坐标点
    rect = np.zeros((4,2), dtype='float32')

    #　按照书序找到对应坐标0123分别 左上，右上，左下，右下

    # 计算左上，右上
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # 计算左下，右上
    diff = np.diff(pts,axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]


    return rect

def four_point_transform(image,pts):
    # 获取输入坐标点
    print("1111")
    rect = order_points(pts)
    print(rect)
    (tl,tr,br,bl) = rect
    # print(rect)

    # 计算输入的w和h值
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # 变换后对应坐标位置
    dst = np.array([
        [0,0],
        [maxWidth - 1,0],
        [maxWidth - 1, maxHeight - 1],
        [0,maxHeight -1 ]
    ], dtype="float32")

    # 计算变换矩阵
    M = cv2.getPerspectiveTransform(rect,dst)
    warped = cv2.warpPerspective(image,M,(maxWidth,maxHeight))

    # 返回变换矩阵
    return warped

def sort_contours(cnts,method = "left-to-right"):
    reverse = False
    i = 0
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))
    return cnts, boundingBoxes


# def cv_show(name, img):
#     cv2.imshow(name, img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
def img_f(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray,(5,5),0)
    # cv_show('blurred',blurred)
    edged = cv2.Canny(blurred,50,150)
    # cv_show('edged',edged)
    return edged,gray
def img_lunkuo(imgY,imgG):
    cnts,tee = cv2.findContours(imgG,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgY,cnts,-1,(0,0,255),3


                     )
    # cv_show('contours_img',imgY)
    return imgY,cnts
def f_detail(path):
    # 预处理
    image = cv2.imread(path)
    image = bian.resize(image,width=500)
    # cv_show('image',image)
    contours_img = image.copy()
    img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # cv_show('img',img)
    # r,img = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
    img,gray = img_f(image)
    # cv_show('img',img)
    # 轮廓检测

    img,cnts = img_lunkuo(image,img)
    # cv_show('img2',img )
    docCnt = None
    # print(cnts)
    # 确保检测
    if len(cnts) > 0:
        #　根据轮廓大下进行排序
        cnts = sorted(cnts, key=cv2.contourArea,reverse=True)
        peri = cv2.arcLength(cnts[0],True)
        approx = cv2.approxPolyDP(cnts[0],0.02*peri,True)
        docCnt = approx

    # 执行透视变换
    # print(docCnt)
    warped = four_point_transform(gray,docCnt.reshape(4,2))
    # te = warped.copy()
    warped = cv2.resize(warped,(458,526),interpolation=cv2.INTER_CUBIC)
    # cv_show('warped',warped)
    print(warped.shape)
    print('尺寸')
    # te2 = cv2.Canny(te,50,150)
    # cv_show('te2',te2)
    # te2,cnts=img_lunkuo(warped,te2)
    # cv_show('te2',te2)

    docCnt = None

    # 确保检测
    # if len(cnts) > 0:
    #     #　根据轮廓大下进行排序
    #     cnts = sorted(cnts, key=cv2.contourArea,reverse=True)
    #
    #     # 遍历每一给轮廓
    #     for c in cnts:
    #         # 近似
    #         peri = cv2.arcLength(c,True)
    #         approx = cv2.approxPolyDP(c,0.02 *peri,True)
    #         # print(approx)
    #         # print("qqqqqqqqqqqqqqqqqqqqq")
    #
    #         # 准备做透视变换
    #         if len(approx) == 4:
    #             docCnt = approx
    #             break

    # 执行透视变换
    # print(docCnt)
    # warped = four_point_transform(warped,docCnt.reshape(4,2))
    # cv_show('warped',warped)
    sp = warped.shape
    print(sp)
    sz1 = sp[0]
    sz2 = sp[1]

    a = int(sz1/2)
    b = int(sz1*3/4)
    c = 45
    d = int(sz2)
    warped = warped[a:b,c:d]
    # cv_show('warped2',warped)
    # te = warped.copy()
    # te2 = cv2.Canny(te,50,150)
    # cv_show('te2',te2)
    # te2,cnts=img_lunkuo(warped,te2)
    # cv_show('te2',te2)

    image = bian.resize(warped,width=700)
    # cv_show('image',image)
    sp2 = image.shape
    sz1 = sp2[0]
    sz2 = sp2[1]

    a = int(0)
    b = int(sz1)
    c = 0
    d = int(sz2/5)
    first_line = image[a:b,c:d]
    # cv_show('one2f',first_line)
    two_line = image[a:b,d-8:d*2-8]
    three_line = image[a:b,d*2-8:d*3-8]
    four_line = image[a:b,d*3-12:d*4-12]
    five_line = image[a:b,d*4-12:d*5-12]
    one2f = five_line
    data = [first_line,two_line,three_line,four_line,five_line]
    return data
# Otsu's 阈值处理
def judge(img):
    # cv2.imshow('te',img)
    r,thresh = cv2.threshold(img,125,255,cv2.THRESH_BINARY)
    # cv_show('thresh',thresh)
    thresh_Contours = thresh.copy()


    # 找到每一个圆圈轮廓
    cnts,tee = cv2.findContours(thresh_Contours,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cv2.drawContours(img,cnts,-1,(0,255,0),1)
    # cv_show('warped',img)
    questionCnts = []
    # # 遍历
    # print("wqeqwe")
    # print(cnts)
    for c in cnts:
        # 计算比例和大小
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)
        # print(w)
        print("=== ===")
        print(h)
        print("----")
        # prin t(ar)
        # 根据实际 情况指定标准
        if w>=15 and  w<=30  and h <25:
            questionCnts.append(c)
    print("9999999999")
    print(questionCnts)
    # # cv_show('re',questionCnts)
    # 按照从上到下进行排序
    questionCnts = sort_contours(questionCnts,method="right-to-left")[0]
    print(questionCnts)
    correct = 0
    data = {1:5,2:5,3:5,4:5,5:5}
    for (q,i) in enumerate(np.arange(0,len(questionCnts), 4)):
        # 排序
        cnts = sort_contours(questionCnts[i:i + 4])[0]
        bubbled = None
        # 遍历每一个结果
        for (j,c) in enumerate(cnts):
            # 使用mask来判断结果
            mask = np.zeros(thresh.shape, dtype="uint8")
            print('位置')
            print(c[0][0][0])
            print(c[0][0][1])
            if c[0][0][1]>120 and c[0][0][1]<140:
                print('第4行')
                if c[0][0][0]>15 and c[0][0][0]<40:
                    data[4] = 'A'
                elif c[0][0][0]>40 and c[0][0][0]<60:
                    data[4] = 'B'
                elif c[0][0][0]>65 and c[0][0][0]<93:
                    data[4] = 'C'
                elif c[0][0][0] > 95 and c[0][0][0] < 120:
                    data[4] = 'D'
            elif c[0][0][1]>80 and c[0][0][1]<110:
                print('第三行')
                if c[0][0][0]>15 and c[0][0][0]<40:
                    data[3] = 'A'
                elif c[0][0][0]>40 and c[0][0][0]<60:
                    data[3] = 'B'
                elif c[0][0][0]>65 and c[0][0][0]<93:
                    data[3] = 'C'
                elif c[0][0][0] > 95 and c[0][0][0] < 120:
                    data[3] = 'D'
            elif c[0][0][1]>10 and c[0][0][1]<40:
                print('第一行')
                if c[0][0][0]>15 and c[0][0][0]<40:
                    data[1] = 'A'
                elif c[0][0][0]>40 and c[0][0][0]<60:
                    data[1] = 'B'
                elif c[0][0][0]>65 and c[0][0][0]<93:
                    data[1] = 'C'
                elif c[0][0][0] > 95 and c[0][0][0] < 120:
                    data[1] = 'D'

            elif c[0][0][1]>50 and c[0][0][1]<70:
                print('第二行')
                if c[0][0][0]>15 and c[0][0][0]<40:
                    data[2] = 'A'
                elif c[0][0][0]>40 and c[0][0][0]<60:
                    data[2] = 'B'
                elif c[0][0][0]>65 and c[0][0][0]<90:
                    data[2] = 'C'
                elif c[0][0][0] > 95 and c[0][0][0] < 120:
                    data[2] = 'D'
            elif c[0][0][1] > 150 and c[0][0][1] <180:
                print('第五行')
                if c[0][0][0] > 15 and c[0][0][0] < 40:
                    data[5] = 'A'
                elif c[0][0][0] > 40 and c[0][0][0] < 60:
                    data[5] = 'B'
                elif c[0][0][0] > 65 and c[0][0][0] < 90:
                    data[5] = 'C'
                elif c[0][0][0] > 95 and c[0][0][0] < 120:
                    data[5] = 'D'
            print(c)
            # cv2.drawContours(mask,[c], -1, 255,-1 )# -1表示填充
            # cv_show
    sorted(data.keys())
    return data



# one = judge(first_line)
# two = judge(two_line)
# three = judge(three_line)
# four = judge(four_line)
# five = judge(five_line)
# data = [one,two,three,four,five]
#
# print(data)














# # 计算轮廓
# threshCnts,hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#

# # 将符合的轮廓从左到右排序
# # print("==========")
# # print(locs)
# # print('++++++++++++')
# # locs = sorted(locs, key=lambda x:x[0])
# # print(locs)
# output = []
# locs.reverse()
# for (i, (gX, gY, gW, gH)) in enumerate(locs):
#     groupOutput = []
#
#     # 根据坐标提取每一个组
#     # cv_show('te',te)
#     group = te[gY-5:gY+gH+5,gX-5:gX+gW+5]
#     # cv_show('group',group)
#
#     # 预处理
#     # print('======')
#     # print(group.shape)
#     # group = cv2.cvtColor(group,cv2.COLOR_BGR2GRAY)
#     # print(group.shape)
#     group = cv2.threshold(group, 0, 255,
#                           cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
#     cv_show('group',group)


        # 通过计算非零点数量计算答案是否正确
#         mask = cv2.bitwise_and(thresh,thresh,mask=mask)
#         total = cv2.countNonZero(mask)
#
#         #通过阈值判断
#         if bubbled is None or total > bubbled[0]:
#             bubbled = (total,j)
#
#     # 对比正确答案
#     color = (0,0,255)
#     k = ANSEER_KEY[q]
#     print("ppppppppp")
#     print(bubbled)
#     print(k)
#     # 判断正确
#     if k == bubbled[1]:
#         color = (0,255,0)
#         correct += 1
#     else:
#         k = bubbled[1]
#
#     # 绘图
#     cv2.drawContours(warped, [cnts[k]], -1, color, 3)
#
# score = (correct / 4.0) * 100
# print("[INFO] score: {:.2f}%".format(score))
# # cv2.putText(warped, "{:.2f}%".format(score), (10, 30),
# # 	cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
# cv2.imshow("Original", image)
# cv2.imshow("Exam", warped)
# cv2.waitKey(0)