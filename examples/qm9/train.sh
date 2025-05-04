#!/bin/bash
export PYTHONPATH=~/LibMTL:$PYTHONPATH
export TMPDIR=/tmp
CUDA_VISIBLE_DEVICES=6 python main.py --weighting MGDA --arch HPS --dataset_path /home/daiheng_zhang_genbio_ai/LibMTL/examples/qm9/qm9_data --gpu_id 6 --mode train --save_path ./result > output_MGDA.log 2>&1