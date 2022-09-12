# LG_instance_segmentation_contest ✨
## 입자 검출 정보 기반으로 입자들의 형태 변화를 계량적 지표로 산출 가능한 모델 개발

---
### Introduction
- 주최 : LG 화학 <br/>
- 주관 : 인공지능팩토리 (AIFactory) <br/>
- 대회 기간: 7/7 (목) 8:00 ~ 8/8 (월) 18:00 <br/>
- link: https://aifactory.space/competition/detail/2067 <br/>
- 주제: 유체상에 떠다니는 입자를 촬영한 화상을 바탕으로 각 입자와 그 형상을 최대한 잘 검출해내는 Instance Segmentation 모델을 만드는 것이 이번 대회 목표. <br/>
- 참고) 입자들의 형상은 균일하지 않고 유체상에서 촬영된 결과물인 만큼 표면으로부터의 거리에 따라 선명도 또한 차이가 있으며, 서로 겹쳐져 있는 경우도 존재. <br/>

<img src='https://user-images.githubusercontent.com/61971952/188265389-b1461854-a775-423b-bd1a-a901de19bef9.png' width = '500' height = '300'/> <br/>

### Dataset
- train dataset: 520장 <br/>
- test dataset: 350장 <br/>
- coco dataset 형식의 annotation file(입자 labeling 형식에 따라 label_train.json, label(polygon)train.json) <br/>
- 객체 category: 1개 (Normal) <br/>
- image height, width = 1024, 1280 <br/>

### Workflow
#### 1주차(7/13 ~ 7/17)
* Studying instance segmentation </br>
(https://mountainous-patio-ee7.notion.site/instance-segmentation-69662f0a591746d2a2db4cb218de95b0) </br> 
* Learn about MMdetection library </br>
간편하게 여러 최신 model을 이용할 수 있도록 package 제공됨. </br>
(https://mountainous-patio-ee7.notion.site/MMdetection-daba1bc939194a999963f4cec999eb59) </br>
* Data analysis 
* Train base-line(Mask RCNN) model <br/>
</br>

 Model | Backbone | Score
 -------------|-------|-------|
 Mask RCNN(base-line) | resnet50 |  0.5761174985  |

</br>

#### 2주차(7/18 ~ 7/24)
* segmentation model list up </br>
→ Mask R-CNN, Cascade Mask R-CNN, Mask Scoring R-CNN, Hybrid Task Cascade, YOLACT, SOLO, PointRend, DetectoRS, SOLOv2, SCNet, QueryInst
* 조원들에게 model 분배 후 제출 </br>
→ ✔️ Model을 분배했던 이유: MMDetection엔 많은 Instance Segmentation model이 존재하는데 각 model을 공부한 다음 data와 맞다고 생각되는 model을 정하기엔 시간이 촉박하여 조원들에게 model 분배 후 performance를 보고 model을 선정하기로 함.
* 점수가 높은 model 선정 </br>
→ SCNet, Mask Scoring R-CNN, Cascade Mask R-CNN, Mask R-CNN  </br>
(0.57 이상의 점수가 나오는 model로 선정)
</br>

selected model | score
-------|-------|
SCNet_r50_fpn_1x_coco  |  0.5861291233  |
Cascade Mask R-CNN_r101_fpn_1x_coco | 0.596460128 |
Mask Scoring R-CNN_r50_fpn_1x_coco | 0.5752475505  |
Mask R-CNN_r101_fpn_1x_coco  |  0.5800140828 |
   
</br>

* model 공부 </br>
  * Mask R-CNN: https://www.notion.so/Mask-R-CNN-36b84ef17a21435e98760b11b444a20c
  * Cascade mask R-CNN: https://www.notion.so/Cascade-R-CNN-67c341f5a30d4c508443c93d3b16c7d6
  * SCNet: https://www.notion.so/SCNet-9d8061d6127b45cebec17e183ab232b8
  * Mask Scoring R-CNN: https://www.notion.so/Mask-Scoring-R-CNN-8db7c7d76c2248f5bcdfb62ee2253674 </br>
* modeling <br/>
최종 선정한 각 모델에서 깊이에 차이를 두고 IoU threshold를 바꿔본 결과 </br> 
cascade_mask_rcnn_x101 모델로 0.6점대를 넘어섰다. </br>
model 과 IoU threshold를 동일 조건으로 줘서 3주차에 전처리과정을 수행할 계획.
</br>

model | epoch | IoU threshold | score
-------|-------|-------|-------|
cascade_mask_rcnn_x101_32x4d_fpn_1x_coco | 12e | 0.3~0.6 | 0.6065363398 |
cascade_mask_rcnn_x101_64x4d_fpn_1x_coco.py | 12e | 0.3~0.6 | 0.6079679485 |

</br>

#### 3주차(7/25 ~ 7/31)
* data 전처리 list up 후 분배, performance 확인 및 선정 </br>
  * Offline augmentation
    * flip, shear, rotate, rotation, bbox flip, bbox rotate, bbox rotation </br>
(cf. rotate vs rotation: 전체 이미지를 돌리는 것, 이미지 사이즈는 고정하되 이미지 자체가 회전되고 남는 부분은 padding 시킴.)
  * Online augmentation </br>
    * shear, rotate, resize, flip, equalize, brightness, contrast, minIoUrandomcrop, Albumentation </br>

</br>

model | online aug | score
-------|-------|-------|
cascade_mask_rcnn_x101_32x4d_fpn_1x_coco | equalize, brightness, contrast | 0.6044010023 |
cascade_mask_rcnn_x101_32x4d_fpn_1x_coco | resize (1024, 1280) | 0.6084128911 |
cascade_mask_rcnn_x101_32x4d_fpn_1x_coco | minIoUrandomcrop | 0.6023441395 |
cascade_mask_rcnn_x101_32x4d_fpn_1x_coco | all augmentation | 0.5452023496 |

</br>
기존의 모델과 비교했을때 performance가 증가하는 건 이미지 원본사이즈로 resize시키는 online augmentation 뿐이었다.
(cf. about offline vs online augmentation: https://yoda-it-study.tistory.com/34 )
 
 ✔️model selection 후 data 전처리 순으로 workflow를 잡은 이유: </br>
 augmentation시 data의 복잡도가 증가하는데 model마다 복잡도도 다양하기 때문에 </br>
 먼저 model을 고정시키고 augmentation을 다양하게 적용시켜 성능향상을 보는것이 좋을거라 판단해 model을 먼저 선택하였다.
* Backbone 분배 후 성능 확인 및 선정 <br/>
  * 최종 backbone: ResNeXt(default), ResNet strikes back 
  * 가장 상위의 performance를 내는 2개의 backbone 선택

</br>

model | online aug | backbone | score
-------|-------|-------|-------|
cascade_mask_rcnn_x101_64x4d_fpn_1x_coco.py | resize(1024, 1280) | ResNeXt(default) | 0.6079679485 |
cascade_mask_rcnn_x101_64x4d_fpn_1x_coco.py | resize(1024, 1280) | resnet strikes back | 0.6045638857 |

</br>

✔️data 전처리 후 backbone selection 순으로 workflow를 잡은 이유: </br>
data augmentation에 따라 data의 complexity에 변화가 생기는데 backbone은 data로 부터 feature map을 뽑아주는 과정이기 때문에 augmentation을 정한 후 그에 맞는 backbone을 선택하는게 좋을거라 판단해 augmentation후 backbone selection을 하였다.

#### 4주차(8/1 ~ 8/8)
* Optimizer 분배 후 선정
  * SGD(default)에서 adadelta로 변경 후 0.61점대를 넘길 수 있었다.
  * adadelta를 최종 optimizer로 선정

<br>

model | online aug | backbone | optimizer | score
-------|-------|-------|-------|-------|
cascade_mask_rcnn_x101_64x4d_fpn_1x_coco.py | resize(1024, 1280) | ResNeXt(default) | adadelta | 0.6104731677	 |
cascade_mask_rcnn_x101_32x4d_fpn_1x_coco.py | resize(1024, 1280) | ResNeXt(default) | adadelta | 0.6110075826	 |
cascade_mask_rcnn_x101_64x4d_fpn_1x_coco.py | resize(1024, 1280) | resnet strikes back | adadelta | 0.6110104141	 |

</br>

* 2주차에서 선택했던 model들에도 동일한 조건으로 둬 performance 확인
<br>

model | online aug | backbone | optimizer | score
-------|-------|-------|-------|-------|
ms_rcnn_x101_64x4d_fpn_1x_coco.py | resize(1024, 1280) | ResNeXt(default) | adadelta | 0.613928616	 |
ms_rcnn_x101_64x4d_fpn_1x_coco.py | resize(1024, 1280) | resnet strikes back | adadelta | 0.6134804408	 |

</br>
cascade mask R-CNN외에도 Mask scoring R-CNN도 높은 성능을 보여주었다. </br>


### Discussion
* IoU threshold 0.2~0.6으로 바꿔주면서 성능이 더 향상되는 것을 확인
<br>

model | online aug | backbone | optimizer | IoU threshold | score
-------|-------|-------|-------|-------|-------|
ms_rcnn_x101_64x4d_fpn_1x_coco.py | resize(1024, 1280) | resnet strikes back | adadelta | 0.3~0.6 | 0.6134804408	 |
ms_rcnn_x101_64x4d_fpn_1x_coco.py | resize(1024, 1280) | resnet strikes back | adadelta | 0.2~0.6 | 0.6171016691	 |

</br>

* epoch 수가 적어짐에 따라 성능이 향상되는 것을 확인
<br>

model | online aug | backbone | optimizer | IoU threshold | epoch | score
-------|-------|-------|-------|-------|-------|-------|
ms_rcnn_x101_64x4d_fpn_1x_coco.py | resize(1024, 1280) | resnet strikes back | adadelta | 0.2~0.6 | 14e | 0.6171016691	 |
ms_rcnn_x101_64x4d_fpn_1x_coco.py | resize(1024, 1280) | resnet strikes back | adadelta | 0.2~0.6 | 10e | 0.6179983076	 |

model | online aug | backbone | optimizer | IoU threshold | epoch | score
-------|-------|-------|-------|-------|-------|-------|
cascade_mask_rcnn_x101_64x4d_fpn_1x_coco.py | resize(1024, 1280) | resnet strikes back | adadelta | 0.2~0.6 | 15e | 0.616678574	 |
cascade_mask_rcnn_x101_64x4d_fpn_1x_coco.py | resize(1024, 1280) | resnet strikes back | adadelta | 0.2~0.6 | 12e | 0.6174024875	 |
cascade_mask_rcnn_x101_64x4d_fpn_1x_coco.py | resize(1024, 1280) | resnet strikes back | adadelta | 0.2~0.6 | 10e | 0.6209292892 |
cascade_mask_rcnn_x101_64x4d_fpn_1x_coco.py | resize(1024, 1280) | resnet strikes back | adadelta | 0.2~0.6 | 9e | 0.623549387 |

</br>

