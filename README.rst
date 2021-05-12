MH5 Robot Combined Documentation
================================

Temporary documentation building for the whole MH5 platform. This collects all the packages used for MH5 and builds a single documentation that is published at `Read The Docs <https://readthedocs.org>`_.

Documentation access
--------------------

To access the documentation `follow this link <https://mh5.readthedocs.io/en/latest/>`_.

You can also access the `PDF format <https://mh5.readthedocs.io/_/downloads/en/latest/pdf/>`_ of the documentation.

.. note:: This documentation is in progress and there will be significant changes in the future as new packages are included and more details are added.

Documentation structure
-----------------------

The documentation uses `Sphinx <https://www.sphinx-doc.org/en/master/>`_ and for C++ code `doxygen <https://www.doxygen.nl/index.html>`_. The formatting is based on the `sphinx-rtd-theme <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_ theme and `breathe <https://breathe.readthedocs.io/en/latest/>`_ is used to bridge the automation of C++ code documentation produced by **doxygen**.

This repository includes a few ``.rst`` files that provide generic information about the project as well as the main structure of the documentation.

In order to make the development and deployment of the various parts of the project manageable they are split in different repositories on GitHub. This repository uses ``git submodule`` functionality to include all these components and then integrates the documentation included in each of the ``docs`` directories into one single structure that is published on ``Read the Docs``.

Documentation build
-------------------

The build is triggered automatically on Read the Docs once any change is performed on the content of this repository.

.. warning:: Due to the way ``submodules`` work in GitHub, changes to the included repositories have to be explicitly pulled in this composite repository to be reflected in the final documentation.
