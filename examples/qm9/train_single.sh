#!/bin/bash
export PYTHONPATH=~/LibMTL:$PYTHONPATH
export TMPDIR=/tmp

# List of target indices to run
targets=(14 15 11)

for target in "${targets[@]}"
do
    echo "Training single task for target $target"
    mkdir -p ./result_single_$target
    CUDA_VISIBLE_DEVICES=5 python main.py \
        --weighting EW \
        --arch HPS \
        --dataset_path /home/daiheng_zhang_genbio_ai/LibMTL/examples/qm9/qm9_data \
        --gpu_id 5 \
        --epochs 200 \
        --target $target \
        --mode train \
        --save_path ./result_single_$target > output_single_$target.log 2>&1
    echo "Finished target $target"
done
