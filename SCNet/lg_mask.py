# 사용할 모델 선택
_base_ = 'configs/scnet/scnet_r50_fpn_1x_coco.py'

checkpoint_config = dict(interval=1, out_dir='/content/drive/MyDrive/KDT/offline/project2/SCNet')
max_epochs= 40
num_last_epochs= 10
# 평가 방법
evaluation = dict(
    metric=['bbox', 'segm'],
    save_best='auto',
    # The evaluation interval is 'interval' when running epoch is
    # less than ‘max_epochs - num_last_epochs’.
    # The evaluation interval is 1 when running epoch is greater than
    # or equal to ‘max_epochs - num_last_epochs’.
    interval=5, 
    dynamic_intervals=[(max_epochs - num_last_epochs, 1)]
    )

# 사전 가중치 사용
load_from = 'checkpoint/scnet_r50_fpn_1x_coco-c3f09857.pth'
#이어서 학습을 하고싶을때 마지막으로  저장된  epoch load
#resume_from = '/content/drive/MyDrive/KDT/offline/project2/SCNet/epoch_1.pth'
# epoch 설정 
runner = dict(type='EpochBasedRunner', max_epochs=max_epochs)

#optimizer
#SGD가 아닌 adadelta를 쓰고싶은 경우
#optimizer = dict(
#    _delete_ = True,
#    type='Adadelta',
#    lr=1.0,
#    rho=0.9,
#    eps=1e-06,
#    weight_decay=0,
#    # foreach=None,
#    # maximize=False
#    )


# batch size 설정
auto_scale_lr = dict(enable=True, base_batch_size=8)

