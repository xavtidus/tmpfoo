import os
import string
import time
import json


WORKING_DIR='tmp/'
os.system("mkdir {}".format(WORKING_DIR))

OUTPUT_S3_BUCKET = 'lego-train-training'

VIDEO_S3_BUCKET = 'lego-train-training'  
VIDEO_S3_KEY = 'videos/rail-racer-train.mp4'

os.system("python3 01_video_to_frame_utils.py --video_s3_bucket {} --video_s3_key {} --working_directory '{}' --visualize_video True --visualize_sample_rate 1 -o '{}'".format( VIDEO_S3_BUCKET, VIDEO_S3_KEY, WORKING_DIR, OUTPUT_S3_BUCKET ))

