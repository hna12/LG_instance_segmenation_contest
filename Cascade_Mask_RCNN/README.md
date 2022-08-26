# Cascade Mask R-CNN

paper link: https://paperswithcode.com/method/cascade-mask-r-cnn

Cascade Mask R-CNN extends Cascade R-CNN to instance segmentation, by adding a mask head to the cascade.

backbone: ResNext101, ResNet strikes back

optimizer: SGD, Adadelta

AutoAugment(transform rather than data augmentation): MinIoURandomCrop, Equailze, Brightness, Contrast, Albumentation(shiftscalerotate, randombrightnesscontrast, RGBshift, Huesaturationvalue), Rotation

img_scale: origin image size = (1280, 1024), default mmdet image size = (1333, 800)
