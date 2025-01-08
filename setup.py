from setuptools import setup

setup(
    name         = "microemu",
    version      = "0.1.2",
    py_modules   = ["microemu"],
    entry_points = {
        "console_scripts": [
            "microemu=microemu:main",
        ],
    },
    description  = "A simple MicroPython emulator",
    license      = "MIT",
    author       = "Volodymyr Shymanskyy",
    author_email = "vshymanskyi@gmail.com",
    url          = "https://github.com/vshymanskyy/microemu",
    classifiers  = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
