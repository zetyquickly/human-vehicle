# human-vehicle
Two-class YOLOv4 based detector

### О решении

Скрипт `apply_net.py` не работает из-за проблем с лейблами в отрисовке https://github.com/pjreddie/darknet/issues/955 . Как достать из darknet какое-то Python API, а не использовать `./darknet` как бинарник, разобраться не удалось 

### Ниже результаты на валидации COCO нейронной сети. 
Короткое описание: Сетка на два класса, обученная на СОСО 2к + 25к итераций

1. Предикт на картинках размера 416x416, AP@0.5

class_id = 0, name = Car, ap = 66.54%            (TP = 1065, FP = 598) 
class_id = 1, name = Person, ap = 77.44%         (TP = 7975, FP = 2766)

2. Предикт на картинках размера 608x608, AP@0.5

class_id = 0, name = Car, ap = 72.24%            (TP = 1150, FP = 506) 
class_id = 1, name = Person, ap = 79.09%         (TP = 8241, FP = 3166)

3. Предикт на картинках размера 608x608, AP@*0.6*

class_id = 0, name = Car, ap = 65.09%            (TP = 1075, FP = 581) 
class_id = 1, name = Person, ap = 73.26%         (TP = 7839, FP = 3568) 

for conf_thresh = 0.25, precision = 0.68, recall = 0.71, F1-score = 0.70 
for conf_thresh = 0.25, TP = 8914, FP = 4149, FN = 3640, average IoU = 56.94 %

### Установка 

1. Пулл докер образа с python2.7 + opencv: `docker pull zetyquickly/human-vehicle`
2. Запуск контейнера `nvidia-docker run --rm  --rm -it zetyquickly/human-vehicle bash` или `docker run --rm --runtime=nvidia -it zetyquickly/human-vehicle bash`
3. Клонируем `https://github.com/AlexeyAB/darknet.git` и запускаем `./build.sh`
4. Устанавливаем `git-lfs`. `curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && apt-get install git-lfs && git lfs install`
5. Клонируем этот репозиторий, и копируем файлы `cp -r human-vehicle/model darknet`, чтобы при запуске бинарника были доступны лейблы для отрисовки
6. Запускаем тест: `./darknet detector test model/obj.data model/yolov4-obj.cfg model/yolov4-obj_best.weights /root/human-vehicle/images/car.jpg -dont_show`
