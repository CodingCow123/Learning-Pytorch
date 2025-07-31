# Learning PyTorch

This repository contains beginner-friendly examples and projects for learning the basics of PyTorch, including:

- Custom datasets and data loaders
- Feedforward neural networks (MLP) for MNIST digit classification
- Convolutional neural networks (CNN) for CIFAR-10 image classification
- Data transformations and visualization
- Training and evaluation loops
- GPU support for Apple Silicon (MPS) and CPU fallback

## Project Structure

```
Learning-Pytorch/
├── datasets_and_dl.py   # Custom dataset and data loader examples
├── feedforward.py       # Feedforward neural network for MNIST
├── cnn.py               # Convolutional neural network for CIFAR-10
├── README.md            # Project documentation
├── .gitignore           # Git ignore rules (excludes datasets)
└── data/                # Downloaded datasets (auto-downloaded, not tracked by git)
```

## Requirements

- Python 3.8+
- PyTorch 1.12+ (with MPS support for Apple Silicon if on Mac)
- torchvision
- matplotlib
- numpy

Install dependencies with:

```bash
pip install torch torchvision matplotlib numpy
```

## Usage

Each script is standalone. For example, to train a feedforward network on MNIST:

```bash
python feedforward.py
```

To train a CNN on CIFAR-10:

```bash
python cnn.py
```

## Notes

- Datasets are automatically downloaded to the `data/` directory if not present.
- The `data/` directory and large dataset files are excluded from git via `.gitignore`.
- Code supports both CPU and Apple Silicon GPU (MPS) automatically.

## License

This project is for educational purposes.

---

**Credit:**
These examples are made from Patrick Loeber's excellent PyTorch tutorial: [PyTorch Beginner Series](https://www.youtube.com/watch?v=c36lUUr864M)
