# Cascade Mask R-CNN

link: https://paperswithcode.com/method/cascade-mask-r-cnn

Cascade Mask R-CNN extends Cascade R-CNN to instance segmentation, by adding a mask head to the cascade.

backbone: ResNet50, ResNet101, ResNext101, ResNet strikes back

optimizer: SGD, Adadelta

AutoAugment: MinIoURandomCrop, Equailze, Brightness, Contrast, Albumentation(shiftscalerotate, randombrightnesscontrast, RGBshift, Huesaturationvalue), Rotation(transform rather than data augmentation)

img_scale: origin image size = (1280, 1024), default mmdet image size = (1333, 800)
