import math
import os.path

import cv2, numpy as np
from sklearn.cluster import KMeans

"""
steal from:
https://stackoverflow.com/questions/43111029/how-to-find-the-average-colour-of-an-image-in-python-with-opencv
"""


def visualize_colors(cluster, centroids):
    # Get the number of different clusters, create histogram, and normalize
    labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    (hist, _) = np.histogram(cluster.labels_, bins=labels)
    hist = hist.astype("float")
    hist /= hist.sum()

    # Create frequency rect and iterate through each cluster's color and percentage
    # rect = np.zeros((50, 300, 3), dtype=np.uint8)
    try:
        colors = sorted([(percent, color) for (percent, color) in zip(hist, centroids)],key=lambda a:a[0],reverse=False)
    except Exception as e:
        print(hist, centroids)
        raise e
    # start = 0
    return colors
    # for (percent, color) in colors:
    #     print(color, "{:0.2f}%".format(percent * 100))
    #     end = start + (percent * 300)
    #     cv2.rectangle(rect, (int(start), 0), (int(end), 50),
    #                   color.astype("uint8").tolist(), -1)
    #     start = end
    # return rect


def averageColorFromFileName(fileName: str):
    """not really average,just pick as a standard"""
    if not os.path.exists(fileName):
        raise FileNotFoundError(fileName + "   does not exist")
    image = cv2.imread(fileName)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    reshape = image.reshape((image.shape[0] * image.shape[1], 3))

    # # Find and display most dominant colors
    try:
        cluster = KMeans(n_clusters=8).fit(reshape)
        visualize = visualize_colors(cluster, cluster.cluster_centers_)
    except Exception as e:
        print(cluster)
        raise e

    expectWeight = .6
    currentWeight = 0.
    arrayCounter = 0
    array = np.array([0.,0.,0.])
    for weight,colorArray in visualize:
        if math.fabs(expectWeight-currentWeight-weight) < math.fabs(expectWeight-currentWeight):
            arrayCounter += 1
            currentWeight += weight
            array += (colorArray*weight)
        else:
            array = array/currentWeight
            array = np.array([math.floor(array[2]),math.floor(array[1]),math.floor(array[0])])
            # image = np.zeros((300, 300, 3), np.uint8)
            # image[:] = array
            # cv2.imshow('visualize', image)
            # cv2.waitKey()
            return array


if __name__ == '__main__':
    print(averageColorFromFileName("textures/textures1214/item/quartz.png"))
