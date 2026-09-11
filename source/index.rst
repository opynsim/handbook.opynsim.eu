Pragmatic Musculoskeletal Modelling
===================================

This handbook sets you up with an open-source software environment and
describes using it to do interesting things with musculoskeletal models.

The OPynSim team maintains this handbook's content `here <https://github.com/opynsim/pragmatic.opynsim.eu>`_
(contributions welcome). In contrast to `OPynSim's documentation <https://docs.opynsim.eu>`_,
this focuses on getting things done using any combination of open-source
projects from the wider ecosystem.
Therefore, while some tasks may indeed use `OPynSim <http://opynsim.eu>`_,
others may use `NumPy <https://numpy.org/>`_,
`OpenSim <https://opensim.stanford.edu/>`_,
`OpenSim Creator <https://opensimcreator.com/>`_, etc. when that's currently
the most pragmatic solution.


Prerequisites
-------------

This handbook assumes:

- You have some familiarity with the `Python <https://python.org>`_ programming language.
- You know how to install Python packages from the command line (e.g. ``pip install numpy``).

If you are unfamiliar with these things, we recommend going through a beginner's Python
course to learn Python and using LLMs to tackle technical/Python problems (e.g. "how
do I install OpenSim into my Python environment").


Handbook Structure
------------------

This handbook is structured into three sections:

- **Setup**: Installing/configuring a computer for musculoskeletal modelling.
- **Concepts**: General concepts/techniques that apply to many musculoskeletal modelling problems/tasks.
- **Guides**: Guides that focus on solving a specific problem/task.

For readers that are new to musculoskeletal modelling, we recommend that
you start by **setting up your system with the core software** and
skimming over some **core concepts** before tackling a **guide**, so
that you encounter fewer technical issues and understand what's going on.

.. toctree::
   :maxdepth: 2
   :caption: Setup
   :hidden:

   setup/core-software
   setup/ides

.. toctree::
   :maxdepth: 2
   :caption: Concepts
   :hidden:

   concepts/core-concepts

.. toctree::
   :maxdepth: 2
   :caption: Guides
   :hidden:

   guides/end-effector-equilibrium-position
   guides/end-effector-ligament-positioning

.. toctree::
   :maxdepth: 2
   :caption: Examples
   :hidden:

.. toctree::
    :caption: Other Links
    :hidden:

    OPynSim GitHub <https://github.com/opynsim/opynsim>
    OpenSim Creator <https://opensimcreator.com>
