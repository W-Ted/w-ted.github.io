import os
import cv2
import numpy as np


# spin
for nn in ['1', '9', '12', '7', 'book']:
    root = f'/export/ywangom/research/nerf/or-nerf/data/spinnerf_dataset/{nn}'
    img_paths = [os.path.join(root,'lama_input', i) for i in sorted(os.listdir(os.path.join(root, 'lama_input'))) if not i.endswith('_mask.png')]
    # print(len(img_paths))
    img_path = img_paths[29]
    mask_path = img_path[:-4] + '_mask.png'
    assert os.path.exists(img_path), img_path
    assert os.path.exists(mask_path), mask_path
    
    img = cv2.imread(img_path).astype(np.float32)
    mask = cv2.imread(mask_path).astype(np.float32)
    # print(img.shape, img.dtype, img.min(), img.max())
    # print(mask.shape, mask.dtype, mask.min(), mask.max())
    h, w, _ = img.shape

    new_h, new_w = int(h/3), int(w/3)

    mask_resize = cv2.resize(mask, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)
    # print(mask_resize.shape, mask_resize.dtype, mask_resize.min(), mask_resize.max())
    img[-new_h:,-new_w:,:] = mask_resize
    cv2.imwrite(f'{nn}.jpg', img)

    # exit()
    


# # qq
for nn in ['qq10']:
    root = f'/export/ywangom/research/nerf/or-nerf/data/ibrnet_data/{nn}'
    img_paths = [os.path.join(root,'images_1', i) for i in sorted(os.listdir(os.path.join(root, 'images_1'))) if not i.endswith('_mask.png')]
    img_path = img_paths[0]
    mask_paths = [os.path.join(root,'masks', i) for i in sorted(os.listdir(os.path.join(root, 'masks'))) if not i.endswith('_mask.png')]
    mask_path = mask_paths[0]
    assert os.path.exists(img_path), img_path
    assert os.path.exists(mask_path), mask_path
    
    img = cv2.imread(img_path).astype(np.float32)
    mask = cv2.imread(mask_path).astype(np.float32)
    # print(img.shape, img.dtype, img.min(), img.max())
    # print(mask.shape, mask.dtype, mask.min(), mask.max())
    h, w, _ = img.shape

    new_h, new_w = int(h/3), int(w/3)

    mask_resize = cv2.resize(mask, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)
    # print(mask_resize.shape, mask_resize.dtype, mask_resize.min(), mask_resize.max())
    img[-new_h:,-new_w:,:] = mask_resize
    cv2.imwrite(f'{nn}.jpg', img)

