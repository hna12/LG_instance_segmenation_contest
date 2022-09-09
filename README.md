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
(https://mountainous-patio-ee7.notion.site/MMdetection-daba1bc939194a999963f4cec999eb59) </br>
* Data analysis 
* Training base-line(Mask RCNN) model <br/>

#### 2주차(7/18 ~ 7/24)
segmentation model 조원들에게 분배 후 제출해 점수가 높은 model 선정 후 model 공부, modeling <br/>
#### 3주차(7/25 ~ 7/31)
Augmentation(이미지 증강 기법)을 listup 하여 각각 어떤 증강 기법을 사용할지 분배 후 성능 확인 및 선정. <br/>
Backbone 분배 후 성능 확인 및 선정 <br/>
#### 4주차(8/1 ~ 8/8)
Optimizer, Lr-scheduler 분배 후 선정 <br/>
성능 향상을 위한 hyperparameter 조정 <br/>

### Result
- mmdetection설명
- segmentation model -> 선정한 model
- augmentation list up -> 선정한거
- backbone 
- optimizer, lr-scheduler
- hyperparameter


## Discussion
