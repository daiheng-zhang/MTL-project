### Run a Model

The complete training code for the NYUv2 dataset is below:

```shell
python main.py --weighting EW --arch HPS --dataset_path /path/to/nyuv2 --gpu_id 0 --scheduler step --mode train --save_path PATH
```

Here the --weighting EW can also be MGDA or Gradnorm.

For training QM9 dataset, we can use:


```shell
python main.py --weighting EW --arch HPS --dataset_path PATH --gpu_id GPU_ID --target TARGET --mode train --save_path PATH
```
Here the --weighting EW can also be MGDA or Gradnorm.

The reproduced result for NYUv2 dataset can be refered here: https://drive.google.com/drive/folders/1yVBgncPqMyhwFOr4A0buM6zhOxW_wJYe?usp=sharing.

The code is mostly based on https://github.com/median-research-group/LibMTL.
