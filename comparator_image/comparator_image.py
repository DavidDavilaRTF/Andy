from PIL import Image
import imagehash
import numpy
import pandas

img_1 = Image.open('C:/Users/hp/Desktop/CaptureDY.JPG')
img_1 = numpy.array(img_1)
img_2 = Image.open('C:/Users/hp/Desktop/CaptureDY.JPG').convert('LA')
img_2 = numpy.array(img_2)
def convolution_2D(mat,mod):
    res_x = 0 * mat
    res_y = 0 * mat
    res = 0 * mat
    len_conv = 1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i-len_conv >= 0 and j-len_conv >= 0 and i+len_conv < len(mat) and j+len_conv < len(mat[0]):
                for k in range(len(mat[0][0])):
                    if mod == 1:
                        res[i,j,k] = max(0,- mat[i-1,j-1,k] - mat[i-1,j,k] - mat[i-1,j+1,k] \
                                    - mat[i+1,j-1,k] - mat[i+1,j,k] - mat[i+1,j+1,k] \
                                    - mat[i,j-1,k] + 8 * mat[i,j,k] - mat[i,j+1,k])
                    elif mod == 2:
                        res[i,j,k] = - mat[i-1,j-1,k] - mat[i-1,j,k] - mat[i-1,j+1,k] \
                                    + mat[i,j-1,k] + mat[i,j,k] + mat[i,j+1,k]
                    elif mod == 3:
                        res[i,j,k] = - mat[i+1,j-1,k] - mat[i+1,j,k] - mat[i+1,j+1,k] \
                                    + mat[i,j-1,k] + mat[i,j,k] + mat[i,j+1,k]
                    elif mod == 4:
                        res[i,j,k] = mat[i,j,k] + mat[i+1,j,k] + mat[i-1,j,k] \
                                    - mat[i,j+1,k] + mat[i+1,j+1,k] + mat[i-1,j+1,k]
                    elif mod == 5:
                        res[i,j,k] = mat[i,j,k] + mat[i+1,j,k] + mat[i-1,j,k] \
                                    - mat[i,j-1,k] + mat[i+1,j-1,k] + mat[i-1,j-1,k]
                    elif mod == 6:
                        res[i,j,k] = - mat[i-1,j,k] \
                                    - mat[i,j-1,k] + 4 * mat[i,j,k] - mat[i,j+1,k] \
                                    - mat[i+1,j,k]
                    elif mod == 7:
                        res[i,j,k] = mat[i-1,j,k] - 2 * mat[i-1,j+1,k] + mat[i-1,j+1,k] \
                                    - 2 * mat[i,j-1,k] + 4 * mat[i,j,k] - 2 * mat[i,j+1,k] \
                                    + mat[i+1,j,k] - 2 * mat[i+1,j+1,k] + mat[i+1,j+1,k]
                    elif mod == 8:
                        res[i,j,k] = mat[i-1,j,k] \
                                    + mat[i,j-1,k] - 4 * mat[i,j,k] + mat[i,j+1,k] \
                                    + mat[i+1,j,k]
                    elif mod == 9:
                        x = 0.5 * (mat[i,j+1,k] - mat[i,j-1,k])
                        y = 0.5 * (mat[i+1,j,k] - mat[i-1,j,k])
                        res[i,j,k] = numpy.power(x*x + y*y,0.5)
                    elif mod == 10:
                        res[i,j,k] = 0.5 * (mat[i,j+1,k] - mat[i,j-1,k])
                    elif mod == 11:
                        res[i,j,k] = 0.5 * (mat[i+1,j,k] - mat[i-1,j,k])
    return res
for i in range(1,5):
    img = convolution_2D(img_1,i)
    img = Image.fromarray(img * 255)
    img.save('C:/Users/hp/Desktop/' + str(i) + '.png')
