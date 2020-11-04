import cv2
import numpy as np
import glob
import time
import multiprocessing
import threading

"""
Sequentiall on single core
"""


def merge(list1, list2): 
	
	merged_list = [[list1[i], list2[i]] for i in range(0, len(list1))] 
	return merged_list 
	


def filebrowser(ext='', directory=''):
    """
    returns files with an extension
    """
    return [f for f in glob.glob(f"{directory}**/*{ext}", recursive=True)]

image_dir = filebrowser(ext='.jpeg', directory='') # directory='' ==> search images from current to inner sub-directories
image_dir += filebrowser(ext='.jpg', directory='')

#print(image_dir)


image_name = 'image_08173.jpg' # origional image path goes here
original = cv2.imread(image_name) 


start_time = time.time()
time_list = ()
image_count = 1
image_count_list = ()
for image_ in image_dir:
    try:
        image_to_compare = cv2.imread(image_)
        if original.shape == image_to_compare.shape:

            difference = cv2.subtract(original, image_to_compare)
            b, g, r = cv2.split(difference)

            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:

                sift = cv2.xfeatures2d.SIFT_create()
                kp_1, desc_1 = sift.detectAndCompute(original, None)
                kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

                index_params = dict(algorithm=0, trees=5)
                search_params = dict()
                flann = cv2.FlannBasedMatcher(index_params, search_params)

                matches = flann.knnMatch(desc_1, desc_2, k=2)

                good_points = []
                for m, n in matches:
                    if m.distance < 0.6*n.distance:
                        good_points.append(m)

                # Define how similar they are
                number_keypoints = 0
                if len(kp_1) <= len(kp_2):
                    number_keypoints = len(kp_1)
                else:
                    number_keypoints = len(kp_2)

        time_list += (round(time.time() - start_time, 5), )
        image_count_list += (image_count, )

        image_count += 1
    except Exception as e:
        pass



print("--- %s seconds ---" % (time.time() - start_time))
print('Program Executed Completely')
# print(time_list)
# print(image_count_list)
l = merge(image_count_list,time_list)
print(l)