#!/bin/bash
export PYTHONPATH=~/LibMTL:$PYTHONPATH
export TMPDIR=/tmp
CUDA_VISIBLE_DEVICES=4 python main.py --weighting EW --arch HPS --dataset_path /home/daiheng_zhang_genbio_ai/LibMTL/examples/qm9/qm9_data --gpu_id 4 --mode train --save_path ./result 