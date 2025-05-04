#!/bin/bash
export PYTHONPATH=~/LibMTL:$PYTHONPATH
export TMPDIR=/tmp
CUDA_VISIBLE_DEVICES=7 python main.py --weighting WEIGHTING --arch ARCH --dataset DATASET --dataset_path PATH --gpu_id GPU_ID --multi_input --save_path PATH --mode train > output_GradNorm.log 2>&1