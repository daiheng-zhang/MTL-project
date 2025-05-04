#!/bin/bash
export PYTHONPATH=~/LibMTL:$PYTHONPATH
export TMPDIR=/tmp
CUDA_VISIBLE_DEVICES=7 python main.py --weighting GradNorm --single_task normal --arch HPS --dataset_path ./nyuv2 --gpu_id 7 --scheduler step --mode train --save_path ./nyuv2_output > output_GradNorm_single_normal.log 2>&1