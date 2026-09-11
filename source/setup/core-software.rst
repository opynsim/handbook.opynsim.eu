Core Software
=============

This section guides the setup of the core software used throughout this handbook.

All code in this handbook is written in `Python <https://www.python.org/>`_.
The following libraries are considered core:

- `Matplotlib <https://matplotlib.org/>`_: For plotting and visualization
- `NumPy <https://numpy.org/>`_: For numerical computing (vectors, matrices)
- `Pandas <https://pandas.pydata.org/>`_: For tabular data manipulation (dataframes).
- `OpenSim <https://opensim.stanford.edu/>`_ + `OPynSim <https://opynsim.eu>`_: For musculoskeletal modelling.

Matplotlib, NumPy, and Pandas ensure good interoperability with the
broader scientific Python ecosystem. OpenSim is chosen because it has
been used in musculoskeletal modelling for 15+ years. OPynSim (developed
by the guide's maintainers) streamlines specific modeling workflows,
particularly data and output extraction.

Set Up Python Environment
-------------------------

Before running any code in this handbook, you need a working Python installation
and virtual environment. This has three primary steps:

1. **Install Python**: Download and install a supported Python version (3.10+ recommended)
   for your operating system.
2. **Create a Virtual Environment**: Use Python's built-in ``venv`` module to initialize
   an isolated virtual environment directory for this project. Most developer IDEs (e.g.
   Visual Studio Code, PyCharm) expect the directory to be called ``.venv/``.
3. **Activate and Install Dependencies**: Activate the environment within your terminal session
   and use ``pip`` to install the core libraries (NumPy, Pandas, Matplotlib, OpenSim, OPynSim).

Follow the steps below corresponding to your operating system to complete the setup.

.. note:: Why Use a Virtual Environment?

   A virtual environment is a self-contained directory that holds a specific version
   of Python and its installed packages. Isolating your dependencies prevents version
   conflicts between this handbook's code and other Python projects on your system.
   It also ensures that updating a system-wide library will not break your setup.


High-Level Setup Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~



Set Up Python Environment
-------------------------

The first thing you should set up Python.


Set Up IDE/Development Environment
----------------------------------
