"""Top-level package for sea-names."""

__author__ = """Luke Campbell"""
__email__ = "luke@axds.co"
__version__ = "0.4.0"

from .geo import (
    get_region_polygons,
    get_sea_bounds,
    get_sea_name,
    get_sea_names_for_trajectory,
)


__all__ = [
    "get_sea_bounds",
    "get_region_polygons",
    "get_sea_name",
    "get_sea_names_for_trajectory",
]
