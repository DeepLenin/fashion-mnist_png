# [Fashion-MNIST] converted to png

This repo contains the following:

- Simple script to convert MNIST-like datasets to png images.

- [Fashion-MNIST] converted to png format stored in the `data.zip` file.

## Why

I was needed Fashion-MNIST dataset for cool simplified example of DL framework
usage, and I want to make it as close to usual Kaggle-like dataset workflow as
possible.

Sometimes you just don't want all this parsing stuff.

I was about to fork one of repos or gists ([1], [2], [3]) which convert original
MNIST into png images. But some of them don't have licenses, some
have too
restricted as for me. That's why I've written this script under MIT
license.

## Usage

### Dataset

[Download `data.zip` file](https://github.com/DeepLenin/fashion-mnist_png/raw/master/data.zip)

Unzip it and you good to go:

```
unzip data.zip
```

The structure of the `data` directory after unzip is following:

```
data
├── test
│   ├── 0
│   ├── 1
│   ├── 2
│   ├── 3
│   ├── 4
│   ├── 5
│   ├── 6
│   ├── 7
│   ├── 8
│   └── 9
└── train
    ├── 0
    ├── 1
    ├── 2
    ├── 3
    ├── 4
    ├── 5
    ├── 6
    ├── 7
    ├── 8
    └── 9
```

Images in those directories named independently from directory structure,
so if you merge all those folders in one - none of images will be overwritten.

Names are from `0.png` to `59999.png` for `train` folder and from `0.png`
to `9999.png` for `test`.

### Script

In case if you want to convert MNIST or other MNIST-similar dataset like
Fashion-MNIST - you can use `mnist_to_png.py` script.

There are lots of hard coded stuff, but it's easy to tweak if you need.

But it should work as is if you put your MNIST files into `original_data` folder in
root of this repo:

```bash
original_data
├── train-images-idx3-ubyte.gz
├── train-labels-idx1-ubyte.gz
├── t10k-images-idx3-ubyte.gz
└── t10k-labels-idx1-ubyte.gz
mnist_to_png.py
```

Then just run:

```bash
python3 mnist_to_png.py
```

And it will create `data` directory with all the images stored according to
structure above.

Feel free to ask for help in [issues](https://github.com/DeepLenin/fashion-mnist_png/issues/new).

## Requirements

I've tried to minimize requirements for this script:

- Python 3+
- [pypng]

You can install them by:

```bash
pip install -r requirements.txt
```

## Licenses

[This project License (MIT)](https://github.com/DeepLenin/fashion-mnist_png/blob/master/LICENSE)

[Fashion-MNIST License (MIT)](https://github.com/zalandoresearch/fashion-mnist/blob/master/LICENSE)

[1]: https://github.com/myleott/mnist_png
[2]: https://github.com/pjreddie/mnist-csv-png
[3]: https://gist.github.com/fukuroder/caa351677bf718a8bfe6265c2a45211f
[pypng]: https://github.com/drj11/pypng
[Fashion-MNIST]: https://github.com/zalandoresearch/fashion-mnist

## Copyright notice

Fashion-MNIST: Copyright © 2017 Zalando SE, https://tech.zalando.com
