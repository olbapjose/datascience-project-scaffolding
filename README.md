# datascience-project-scaffolding
Repo structure for Data Science projects planned to go into production


## Project structure

* `config`: a folder for properties files where paths, constants or any configuration parameters are defined
* `notebooks`: this folder is NOT part of the package. It should contain notebooks that just try out the functions of
   our package, but do not generally implement useful things. The notebook just calls the useful functions that are
   implemented in the jobs or in the project_tools submodule.
* `my_package`: the Python package main folder (rename to the proper package name, here and in the `setup.py` file).
  * `jobs`: subpackage that contains small python files that launch each stage of a project. Ideally, these files
  should basically call a few functions defined in the `project_tools` module, so the jobs should be small files.
    * `main_job.py`: this is the entry point of the package. The user should invoke this file with the proper
    command line arguments to indicate which stage must be launched (EDA, feature creation -which includes 
    preprocessing, but could be a separate job as well-, training, etc.). E.g. `python main_job.py predict`.
    The main function of this file can also be called from within a notebook, instead of using the command line,
    if the package is properly imported in the notebook cell.
  * `project_tools`: a helper module that contains most of the useful code. Each file of this module must contain
  a number of functions that actually apply the Data Science procedures. Ideally, the jobs should call the functions
  of those files. 
* `tests`: it should contain .py files containing software unit tests. This folder is optional if the project has no tests.


## Generation of the wheel file

The Python package file can be generated (wheel file) with 

`python setup.py bdist_wheel`. 

This will create two new folders, one of them called `dist` that contains the .whl file that can be installed with 

`pip install ruta_fichero_wheel.whl`, 

or it can be uploaded to our Databricks cluster (even if we do not need Spark in our project, we can still use a Databricks notebook to
call the functions of our package, provided the package has been installed in our cluster - via the `Libraries` tab)