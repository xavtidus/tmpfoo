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

filen = args["source_key"].split('.')[0]

os.system("aws s3 sync {}/{} s3://{}/frames/ ".format( args["work_dir"], filen, args["output_bucket"] ))

os.system("python3 02_generate_gt_manifest.py -b {} -k {} -d {} -r {}".format( args["output_bucket"], "frames/", args["work_dir"], 5 ))

os.system("aws s3 cp {}/ground_truth_manifest.json s3://{}/ground_truth/".format( args["work_dir"], args["output_bucket"] ))

os.system("python3 03_visualize_gt_labeling_manifest.py -b {} -k {} -i {}{}".format( args["output_bucket"], "ground_truth/ground_truth_manifest.json", args["work_dir"], filen ))

os.system("aws s3 cp {}/ground_truth_manifest_preview.png s3://{}/ground_truth/".format( args["work_dir"], args["output_bucket"] ))

#os.system("aws ec2 terminate-instances --instance-ids 'curl http://169.254.169.254/latest/meta-data/instance-id'")
