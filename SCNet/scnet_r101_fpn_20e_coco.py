_base_ = './scnet_r50_fpn_20e_coco.py'
#ResNet 101의 경우
model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')))
