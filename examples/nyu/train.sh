#!/bin/bash
export PYTHONPATH=~/LibMTL:$PYTHONPATH
export TMPDIR=/tmp
CUDA_VISIBLE_DEVICES=5 python main.py --weighting GradNorm --single_task depth --arch HPS --dataset_path ./nyuv2 --gpu_id 5 --scheduler step --mode train --save_path ./nyuv2_output > output_GradNorm_single_segment.log 2>&1