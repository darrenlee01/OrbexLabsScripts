# tests the amount that the images can be compressed before the comparison
#   values significantly deviate from reality. Testing to see the optimal
#   compression that weighs both accuracy and optimization into consideration
#
#   Created by: Darren Lee

import cv2, numpy, os, time
from PIL import Image as im
from skimage.metrics import structural_similarity as ssim

# comparison function
def compare_images(image1, image2):
    ssimVal = ssim(image1, image2)

    return ssimVal

# finding comparison failure point
def testCompressionFailurePoint(imgPath1,
        imgPath2,
        dim1 = [0, 350, 0, 866], 
        dim2 = [350, 700, 0, 866],
        thresh = 0.95):

    origImage1 = cv2.imread(imgPath1)
    origImage2 = cv2.imread(imgPath2)

    image_a = origImage1[dim1[0]:dim1[1], dim1[2]:dim1[3]]
    image_b = origImage2[dim2[0]:dim2[1], dim2[2]:dim2[3]]

    im.fromarray(image_a).show()
    im.fromarray(image_b).show()


    image_a = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
    image_b = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)


    times = []


    reduction_factor = 1

    while (reduction_factor > 0.05):

        print(reduction_factor)

        dimensions = (int(image_a.shape[1] * reduction_factor), 
                    int(image_a.shape[0] * reduction_factor))
        
        print(dimensions)

        smaller_image_a = cv2.resize(image_a, dimensions, interpolation=cv2.INTER_AREA)
        smaller_image_b = cv2.resize(image_b, dimensions, interpolation=cv2.INTER_AREA)

        if (reduction_factor == 0.1):
            im.fromarray(smaller_image_a).show()
            im.fromarray(smaller_image_b).show()

        start_time = time.time()
        compare_val = compare_images(smaller_image_a, smaller_image_b)
        totalTime = time.time() - start_time
        
        print("Time:", totalTime)
        times.append(totalTime)

        print("Comparison Val:", compare_val)

        if (compare_val >= thresh):
            print("failed at", reduction_factor)

        print("\n\n")

        reduction_factor -= 0.1

        reduction_factor = round(reduction_factor, 3)
    


    startReduction = 1
    for eachTime in times:
        print("Comparison with " + str(startReduction) + " reduction:", eachTime)
        startReduction -= 0.1
        startReduction = round(startReduction, 2)

        
        

# tests the time optimization after compressing the images by a given factor
def testCompressedResponseTime(reduction_factor = 0.2):

    origImage = cv2.imread("C:\\Users\\Darren\\Downloads\\Scratch.jpg")

    image_a = origImage[0:350, 0:866]
    image_b = origImage[350:700, 0:866]

    image_a = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
    image_b = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)

    assert(image_a.shape[0] == image_b.shape[0])
    assert(image_a.shape[1] == image_b.shape[1])


    start_time = time.time()
    compare_images(image_a, image_b)
    end_time = time.time()


    print("original pic time used:", end_time - start_time)

    dimensions = (int(image_a.shape[1] * reduction_factor), 
                    int(image_a.shape[0] * reduction_factor))

    smaller_image_a = cv2.resize(image_a, dimensions, interpolation=cv2.INTER_AREA)
    smaller_image_b = cv2.resize(image_b, dimensions, interpolation=cv2.INTER_AREA)


    start_time = time.time()
    compare_images(smaller_image_a, smaller_image_b)
    end_time = time.time()


    print("Compressed by", reduction_factor, "pic time used:", end_time - start_time)




#testCompressedResponseTime()

"""
testCompressionFailurePoint(imgPath1 = "C:\\Users\\Darren\\Downloads\\Scratch.jpg",
        imgPath2 = "C:\\Users\\Darren\\Downloads\\Scratch.jpg",
        dim1 = [0, 350, 0, 866], 
        dim2 = [350, 700, 0, 866],
        thresh = 0.95)
"""

"""
testCompressionFailurePoint(imgPath1 = "/Users/darrenlee/Desktop/schedule.jpg",
        dim1 = [0, 350, 0, 866], 
        imgPath2 = "/Users/darrenlee/Desktop/schedule.jpg",
        dim2 = [0, 350, 0, 866],
        thresh = 0.95)
"""



'''
imgpath = "C:\\Users\\Darren\\Downloads\\Capture.png"
frame = cv2.imread(imgpath)

im.fromarray(frame).show()

origHeight = frame.shape[0]
origWidth = frame.shape[1]

ratio = 0.1
dimensions = (int(frame.shape[1] * 0.1), int(frame.shape[0] * ratio))
frame = cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

im.fromarray(frame).show()

dimensions = (origWidth, origHeight)
frame = cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


im.fromarray(frame).show()
'''

