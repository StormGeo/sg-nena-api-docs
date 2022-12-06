![](images/Frame_108.png)

# Tutorials and Power Query scripts for the StormGeo Nena API.

Here you will find material related to the StormGeo Nena API. This included an interactive python notebook tutorial that will teach you how to use the
Nena API with Python and JupyterLab. You will also find Power Query scripts to connect the Nena API with Excel.

To get the files in this repository:

1. Clone the repository or download it as a zip file.

## Power Query

In the Power Query folder, you will find the three Power Query functions to import into Excel. Please see the [API documentation](https://docs.nena.no/api/) on how to setup [Power Query](https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query).

## Jupyter Notebook tutorial

The notebook tutorials can be found in the Tutorials folder.

### Requirements

You will need the following packages to run the notebook tutorials:

- JupyterLab
- Python3
- Pandas
- Matplotlib

The easiest way to get these is by using a default installation of [Anaconda](https://www.anaconda.com/).

## API Limitations

Here are listed a few important limitations in the API that any user should be aware of.

- Due to limitations in the API, there are 24 hour values in both DST clock change days, with the missing hour being averaged into 02:00 for autumn, and an interpolated extra hour on the spring clock change

## Contact

If you have any questions, please don't hesitate to contact us at
nena@stormgeo.com
