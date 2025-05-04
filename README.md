### Run a Model

The complete training code for the NYUv2 dataset is provided in [examples/nyu](./examples/nyu). The file [main.py](./examples/nyu/main.py) is the main file for training on the NYUv2 dataset.

You can find the command-line arguments by running the following command.

```shell
python main.py -h
```

For instance, running the following command will train an MTL model with EW and HPS on NYUv2 dataset.

```shell
python main.py --weighting EW --arch HPS --dataset_path /path/to/nyuv2 --gpu_id 0 --scheduler step --mode train --save_path PATH
```

More details is represented in [Docs](https://libmtl.readthedocs.io/en/latest/docs/getting_started/quick_start.html).
