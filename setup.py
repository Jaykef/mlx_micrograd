import setuptools
from pathlib import Path

root_dir = Path(__file__).parent
requirements_path = root_dir / "requirements.txt"
with open(requirements_path) as fid:
    requirements = [l.strip() for l in fid.readlines()]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mlx_micrograd",
    version="0.1.0",
    author="Jaward Sesay",
    author_email="jawardsesay1996@gmail.com",
    description="An mlx port of Karpathy's micrograd - a tiny scalar-valued autograd engine with a small PyTorch-like neural network library on top.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jaykef/mlx_micrograd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)
