import multiprocessing
from multiprocessing.pool import ThreadPool
from tqdm import tqdm
import os, sys, argparse

parser = argparse.ArgumentParser(description='Apply HUmanVehicle darknet model on folder')
parser.add_argument('--images_dir', type=str,
                    help='path to image folder')
parser.add_argument('--output_dir', type=str,
                    help='path to output folder')
parser.add_argument('--thresh', type=float, default=0.8,
                    help='IoU threshold during prediction')    

opt = parser.parse_args()

if __name__ == "__main__":

    if not os.path.exists(opt.output_dir):
        os.mkdir(opt.output_dir)

    pool_args = [os.path.join(opt.images_dir, fname) for fname in os.listdir(opt.images_dir)]

    results = []
    for arg in pool_args:
        cmd = "darknet detector test model/coco.data model/yolov4-obj.cfg model/yolov4-obj_best.weights-dont_show {} -thresh {}".format(arg, opt.thresh)
        popen = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        popen.wait()

