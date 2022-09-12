# SCNet
paper link: https://ojs.aaai.org/index.php/AAAI/article/view/16374/16181

backbone: ResNet50, ResNet101, ResNext101

optimizer: SGD, Adadelta

AutoAugment: MinIoURandomCrop (online augmentation)

img_scale: origin image size = (1280, 1024), default mmdet image size = (1333, 800)
