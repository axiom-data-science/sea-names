
.. image:: http://git.axiom/axiom/sea-names/badges/main/pipeline.svg
   :alt: Pipeline status

sea-names
===============================

Determine the sea-name of any arbitrary point or shapely geometry.

Copyright 2023-2024 Axiom Data Science, LLC

See LICENSE for details.

Installation
------------

This project relies on conda for installation and managing of the project dependencies.

1. Download and install miniconda for your operating system https://docs.conda.io/en/latest/miniconda.html.

2. Clone this project with ``git``.

3.  Once conda is available build the environment for this project with::

      conda env create -f environment.yml

    The above command creates a new conda environment titled ``sea-names`` with the necessary project
    dependencies.

4. An Additional environment file is present for testing and development environments. The additional developer dependencies can be installed with::

      conda env update -f test-environment.yml

5. To install the project to the new environment::

      conda activate sea-names
      pip install -e .


Shapefiles and Dataset Usage
----------------------------

Currently we've been asked to remove the repository of shapefiles used by this library for licensing
reasons. The library will remain publicly accessible but the dataset underlying the library is no
longer available for public distribution.

We are trying to adopt the library to use either an open-source dataset or find alternatives for our
users, we apologize for the inconvenience.


Running Tests
-------------

To run the project's tests::

   pytest -sv --integration

Usage
-----

The package can provide the region name for any given coordinate pair (Longitude, and Latitude).

.. code-block:: python

   import sea_names

   lon = -81.65
   lat = 41.98

   name = sea_names.get_sea_name((lon, lat))
   assert name == "Lake Erie"


The package also has the ability to provide a set of sea names for a series of points. This
capability is still somewhat experimental and can use a lot of memory.

.. code-block:: python

   from sea_names.geo import get_sea_names_for_trajectory
   lons = [
      -176.54,
      -164.70,
      -143.13,
      -126.09,
      -107.18,
      -91.36,
   ]
   lats = [
      55.64,
      48.74,
      56.57,
      45.58,
      21.39,
      25.15,
   ]
   region_names = get_sea_names_for_trajectory(lons, lats, chunk_size=len(lons))
   assert region_names == ['Bering Sea', 'Gulf of Mexico', 'North Pacific Ocean']



Configuration
-------------



Building with Docker
--------------------

To build the docker container::

   docker build -t sea-names .

Running with Docker
-------------------

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
