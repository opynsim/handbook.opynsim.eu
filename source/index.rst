Pragmatic Musculoskeletal Modelling
===================================

This handbook sets you up with an open-source software environment and
describes how you can use it to do interesting things with
musculoskeletal models.

The OPynSim team maintains this project. In contrast to `OPynSim's documentation <https://docs.opynsim.eu>`_,
this focuses on getting things done using any combination of open-source
(esp. Python) projects from the wider ecosystem (contributions welcome).
Therefore, while some tasks may indeed use `OPynSim <https://docs.opynsim.eu>`_,
others may use `NumPy <https://numpy.org/>`_,
`OpenSim <https://simtk.org/api_docs/opensim/api_docs/>`_,
`OpenSim Creator <https://opensimcreator.com/>`_, etc. when it's the most
pragmatic way to get something done.


Prerequisites
-------------

This handbook assumes:

- You can install/setup things on your computer.
- You know how to install Python packages from the command line (e.g. ``pip install numpy``).
- Some familiarity with the `Python <https://python.org>`_ programming language.

The content will try to explain some of these things in passing, but
the explanations won't be as comprehensive as a dedicated guide. In those cases,
we will link to external resources. Alternatively, LLMs are very good at
solving general technical problems (e.g. "how do I install OpenSim into
my Python environment"), so try that if something doesn't make sense.
External contributions (e.g. clarifications) to this handbook are also welcome.

Handbook Structure
------------------

- **Setup**: Installing/configuring a computer for musculoskeletal modelling.
- **Concepts**: General concepts/techniques that apply to many problems/tasks.
- **Guides**: Guides that focus on solving a specific problem/task.
- **Examples**: Standalone examples that perform a specific task.
- **Meta**: Meta documentation for this handbook.

For readers that are new to musculoskeletal modelling, we recommend that
you start by **setting up your system** (at least, with the core software) and
skimming over some **concepts** before tackling a **guide** or **example**, so
that you encounter fewer technical issues and understand what's going on.

.. toctree::
   :maxdepth: 2
   :caption: Setup

.. toctree::
   :maxdepth: 2
   :caption: Concepts

.. toctree::
   :maxdepth: 2
   :caption: Guides

.. toctree::
   :maxdepth: 2
   :caption: Examples

.. toctree::
   :maxdepth: 2
   :caption: Meta
