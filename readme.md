# MDF File Converter

Simple project to convert MF4 files to .mat files. This project is based on Python packages but is bundled as an executable for users who do not have Python installed.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You must have access to windows command prompt to convert files using the executable. You can also call the executable using the bash commands via a Matlab script. See example on how to call an executable using the `system` command [here](https://www.mathworks.com/matlabcentral/answers/4538-how-to-call-an-exe-with-command-line-arguments). To find more information about the Matlab `system` command, look [here](https://www.mathworks.com/help/matlab/ref/system.html).

To convert using the Python scripts/Jupyter Notebook, you can install all the requirements/dependencies using `pip install requirements.txt`. If you do not have a distribution of Python currently installed, you can pick one up [here](https://www.python.org/downloads/). I used Python 3.7.6 for this project. You can also check out Anaconda [here](https://docs.anaconda.com/anaconda/install/), and then install dependencies using `conda create --name MY_ENV --file requirements_conda.txt`, which creates a new virtual environment named MY_ENV. I highly recommend using virtual environments whether using Anaconda or Python.

### Installing

To install, simply clone the repo using `git clone repo_name`, and unzip mdfconverter.zip or mdfconverter2.zip. Inside you will find executables of the same name/
You can call the executables from the command line without having to install any additional programs.

### Examples

I was able to call the mdfconverter version 1 and version 2 using the commands:
`mdfconverter.exe --input_file ../../W810_TSCDV_004.MF4 --output_file ../../test.mat`
`mdfconverter2.exe --input_file ../../W810_TSCDV_004.MF4 --output_file ../../test2.mat`

You can also read the help documentation with `mdfconverter.exe -h`

## Built With

* [asammdf](https://pypi.org/project/asammdf/) - The MDF reader/converter
* [Scipy](https://docs.scipy.org/doc/scipy/reference/index.html) - Scipy io module used to convert Pandas DF to .mat
* [Pandas](https://pandas.pydata.org/) - Used to manipulate MF4 data once loaded
* [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/index.html) - To bundle libs and create executables once completed

## Authors

* **Chris Wernette** - *Initial work*


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to Greg for supplying the MF4 file and giving advice on how to convert/what the desired format is.
