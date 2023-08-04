import numpy as np
import os
import cv2



# head = 'head_v1.0.png'
# mid1 = 'mid1_v1.0.png'
# mid2 = 'mid2_v1.0.png'
# tail = 'tail_v1.0.png'

head = 'Slide1.PNG'
mid1 = 'Slide2.PNG'
mid2 = 'Slide3.PNG'
tail = 'Slide4.PNG'

root_toy = 'toy2_rotation' 
root_scan = 'scannet0113_movement' 

images_all = []
# vid = 'all.mp4'
vid = 'all.avi'

head = cv2.resize(cv2.imread(head), (640*2,480))
mid1 = cv2.resize(cv2.imread(mid1), (640*2,480))
mid2 = cv2.resize(cv2.imread(mid2), (640*2,480))
tail = cv2.resize(cv2.imread(tail), (640*2,480))
# head = cv2.imread(head)
# mid1 = cv2.imread(mid1)
# mid2 = cv2.imread(mid2)
# tail = cv2.imread(tail)

# head
images_all += [head]*40
print(len(images_all))
print(images_all[0].shape)
print(images_all[-1].shape)
# exit()
width,height = 640, 480


# # mid1
images_all += [mid1]*25
print(len(images_all))
print(images_all[0].shape)
print(images_all[-1].shape)


# toy
# idx = [i for i in range(16)]
idx = [i for i in range(1,10)]
idxs = idx + list(reversed(idx)) # 18
idxs = idxs*10 # 180
print(idx)
print(idxs)
files = [os.path.join(root_toy, 'render_%04d.png'%i) for i in idxs] # 180
# imgs = [cv2.imread(file) for file in files]

# debug 1 
# imgs_1 = [cv2.imread(file) for file in files[:18-4]] # 180
# imgs_2 = [imgs_1[-1]]*20 + [cv2.imread('render_0005_highlight.png')] * 45 + [imgs_1[-1]]*20 # stop and hightlight
# imgs_3 = [cv2.imread(file) for file in files[18-4:]] # 180
# imgs = imgs_1 + imgs_2 + imgs_3

imgs_1 = [cv2.imread(file) for file in files[:36-4]] # 180
imgs_2 = [imgs_1[-1]]*20 + [cv2.imread('render_0005_highlight.png')] * 45 + [imgs_1[-1]]*10 # stop and hightlight
imgs_3 = [cv2.imread(file) for file in files[36-4:18*4]] 
imgs_4 = [imgs_3[-1]]*20 + [cv2.imread('render_0001_highlight.png')] * 45 + [imgs_3[-1]]*10 # stop and hightlight
imgs_5 = [cv2.imread(file) for file in files[18*4:]]
imgs = imgs_1 + imgs_2 + imgs_3 + imgs_4 + imgs_5

height,width,layers=imgs[0].shape
images_all += imgs
print(len(images_all))
print(images_all[0].shape)
print(images_all[-1].shape)
# print(len(images_all), height, width)


# mid2
images_all += [mid2]*25
print(len(images_all))
print(images_all[0].shape)
print(images_all[-1].shape)


# scan
idx = [i for i in range(16)]
# idx = [i for i in range(32)]
idxs = idx + list(reversed(idx))
idxs = idxs * 10
files = [os.path.join(root_scan, 'render_%04d.png'%i) for i in idxs]
# imgs = [cv2.imread(file) for file in files]

imgs_1 = [cv2.imread(file) for file in files[:32]] # 180
imgs_2 = [imgs_1[-1]]*20 + [cv2.imread('render_0000_highlight.png')] * 45 + [imgs_1[-1]]*10 # stop and hightlight
imgs_3 = [cv2.imread(file) for file in files[32:]] 
imgs = imgs_1 + imgs_2 + imgs_3

images_all += imgs
print(len(images_all))
print(images_all[0].shape)
print(images_all[-1].shape)

# tail
images_all += [tail]*20
print(len(images_all))
print(images_all[0].shape)
print(images_all[-1].shape)


# video=cv2.VideoWriter(vid,cv2.VideoWriter_fourcc(*'MP4V'),25.0,(width,height))
# video=cv2.VideoWriter(vid,cv2.VideoWriter_fourcc(*'XVID'),25.0,(width,height))
# video=cv2.VideoWriter(vid,cv2.VideoWriter_fourcc(*'XVID'),15.0,(width,height))
# video=cv2.VideoWriter(vid,cv2.VideoWriter_fourcc(*'MP4V'),15.0,(width,height))
video=cv2.VideoWriter(vid,cv2.VideoWriter_fourcc(*'XVID'),15.0,(width,height))

for img in images_all:
    video.write(img)
cv2.destroyAllWindows()
video.release()


