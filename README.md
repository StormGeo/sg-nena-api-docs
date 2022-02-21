![](images/Frame_108.png)

# Documentation and tutorials for the StormGeo Nena API.

Here you will find an interactive python notebook tutorial that will teach you how to use the
Nena API with Python and JupyterLab.

## Getting started

1. Clone the repository or download it as a zip file.

2. Navigate to the directory where you saved the notebook file and start JupyterLab from there.
  If you are using a default installation of Anaconda you should use the Anaconda-Prompt/Anaconda-Powershell.
```
cd <tutorial-notebook-dir>
jupyter lab .
```

## Requirments

You will need:
- JupyterLab
- Python3
- Pandas
- Matplotlib

The easiest way to get these is by using a default installation of [Anaconda](https://www.anaconda.com/).

## API Limitations

Here are listed a few important limitations in the API that any user should be aware of.

* Due to limitations in the API, there are 24 hour values in both DST clock change days, with the missing hour being averaged into 02:00 for autumn, and an interpolated extra hour on the spring clock change


## Contact

If you have any questions, please don't hesitate to contact us at 
nena@stormgeo.com