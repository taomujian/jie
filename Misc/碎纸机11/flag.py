import cv2
import os
import numpy

images = []

def judge(A, B):
    diff = 0
    for r in range(0, len(A)):
        #diff += (A[r][len(A[0]) - 1][0] - B[r][0])[0]
        #diff += (A[r][len(A[0]) - 1][1] - B[r][0])[1]
        diff += (A[r][len(A[0]) - 1][2] - B[r][0])[2] ** 0.25
    return diff

def combine(A, B):
    final_matrix = numpy.zeros((len(A), len(A[0]) + len(B[0]), 3), numpy.uint8)
    final_matrix[0:len(A), 0:len(A[0])] = A
    final_matrix[0:len(A), len(A[0]):len(A[0]) + len(B[0])] = B
    return final_matrix

if __name__ == "__main__":
    f_images = os.listdir("./images")
    for f_image in f_images:
        images.append(
            cv2.imread(
                "images\\" + f_image
            )
        )
    while len(images) > 1:
        min_entropy = -1
        to_combine = None
        for i in range(1, len(images)):
            entropy = judge(images[0], images[i])
            if min_entropy == -1 or entropy < min_entropy:
                min_entropy = entropy
                to_combine = i
        images[0] = combine(images[0], images[to_combine])
        print(len(images), len(images[0][0]))
        images.pop(to_combine)
    cv2.imwrite("./result.png", images[0])