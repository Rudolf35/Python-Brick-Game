# 파이썬으로 제작한 벽돌깨기 게임
파이썬과 pygame 라이브러리를 이용해 만든 간단한 벽돌깨기 게임입니다. 

## 게임 소개
start 버튼을 누르면 3개의 스테이지 중 하나를 선택해 시작할 수 있습니다.

공이 발판의 중앙에 가깝게 맞을수록 수직에 가깝게 공을 튕겨냅니다.

모든 벽돌을 격파하면 클리어가 되고, 스테이지 버튼이 파랗게 변해 클리어한것을 알려줍니다.

## 간단한 활용 방법

### 스테이지 추가 및 조절
main.py에서 스테이지 버튼을 추가하고 위치를 조절해 더 많은 스테이지를 추가할 수 있습니다.
game.py에서 스테이지 번호에 맞는 벽돌 배치를 추가해 주어야 합니다.

### 벽돌 배치
game.py의 bricks 배열을 초기화하는 부분을 수정해 자신이 원하는 벽돌 배치와 벽돌의 속성을 변경할 수 있습니다.
Brick의 멤버를 추가하거나 변경해 더 다양하게 만들 수 있겠죠.

## 추가해볼만한 기능들

### Ball 클래스를 만들고 공의 갯수를 늘려보기

### item 클래스를 만들고 벽돌이 격파되었을 때 확률적으로 아이템 드랍하기
발판의 크기를 늘려주거나, 공을 늘려주는 것 같은 아이템

## 아래는 데모 플레이 이미지입니다.

![Start screen](demo1.jpeg)

![Stage_screen](demo2.jpeg)

![Game_screen1](demo3.jpeg)

![Game screen2](demo4.jpeg)
