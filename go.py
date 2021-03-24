import os
import string
import time
import json
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-w", "--work-dir", required=True, help="the working directory")
ap.add_argument("-o", "--output-bucket", required=True, help="the output s3 bucket")
ap.add_argument("-b", "--source-bucket", required=True, help="the source s3 bucket")
ap.add_argument("-k", "--source-key", required=True, help="the source mp4 key")
args = vars(ap.parse_args())
os.system("mkdir {}".format(args["work_dir"]))

os.system("python3 01_video_to_frame_utils.py --video_s3_bucket {} --video_s3_key {} --working_directory '{}' --visualize_video True --visualize_sample_rate 1 -o '{}'".format( args["source_bucket"], args["source_key"], args["work_dir"], args["output_bucket"] ))

os.system("aws s3 sync {}/{} s3://{}/frames/ ".format( args["work_dir"], args["source_key"].split('.')[0], args["output_bucket"] ))

#os.system("aws ec2 terminate-instances --instance-ids 'curl http://169.254.169.254/latest/meta-data/instance-id'")
