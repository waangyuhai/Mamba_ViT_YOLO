import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolov8n.yaml')
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='')