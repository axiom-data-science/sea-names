"""Module for evaluating the sea names of all points in a trajectory."""
from typing import List

import numpy as np

from shapely.geometry import MultiPolygon, Point


def evaluate_possible_regions(
    sea_bounds: dict, lon: np.ndarray, lat: np.ndarray
) -> List[str]:
    """Return a list of seas where the trajectory intersects the bbox."""
    names = list(sea_bounds.keys())
    # all_bounds is a 2D array of shape (N, 4) where N is the number of regions.
    # all_bounds[i] = [min_x(i), min_y(i), max_x(i), max_y(i)]
    all_bounds = np.array(
        [MultiPolygon(pgon_list).bounds for pgon_list in sea_bounds.values()]
    )
    # LONS is a 2D array of shape (len(all_bounds), len(lons)) where LONS[i, j] = lon[j]
    # LATS is a 2D array of shape (len(all_bounds), len(lats)) where LATS[i, j] = lat[j]
    LONS, _ = np.meshgrid(lon, np.ones(len(all_bounds)))
    LATS, _ = np.meshgrid(lat, np.ones(len(all_bounds)))

    # Create 4 bitmaps that represent the conditions
    # left[i, j] = lon[j] < all_bounds[i, 0]
    # All the longitude points left of the region's leftmost point
    left = LONS < all_bounds[:, 0][:, None]
    # right[i, j] = lon[j] > all_bounds[i, 2]
    # All of the longitude points right of the region's rightmost point
    right = LONS > all_bounds[:, 2][:, None]
    # below[i, j] = lat[j] < all_bounds[i, 1]
    # All of the latitudes below the region's southernmost point
    below = LATS < all_bounds[:, 1][:, None]
    # above[i, j] = lat[j] > all_bounds[i, 3]
    # All of the latitudes above the region's northernmost point
    above = LATS > all_bounds[:, 3][:, None]

    # A unified bitmap representing the points IN the region's bounding box
    # solution[i, j] = True if lon[j] and lat[j] both lie in region[i]'s bounding box.
    solution = (~(left | right)) & (~(above | below))

    # Map the index of each region that's intersected to its name and return the list of those
    # names.
    possible_regions = []
    for i, value in enumerate(np.sum(solution, axis=1) > 0):
        if value:
            possible_regions.append(names[i])
    return possible_regions


def evaluate_polygon_brute_force(
    possible_regions: List[str], lon: np.ndarray, lat: np.ndarray
) -> List[str]:
    """Return the definitive list of regions that intersect that trajectory

    This function evaluates the polygons of each region compared to each point of the trajectory in
    a slow brute-force manner. The fewer the number of possible regions the better this will
    perform.
    """
    from sea_names.geo import get_region_polygons

    valid_regions = []
    # For each of the possible regions check each point in the array to determine if it intersects
    # any of the polygons of the region. A valid region is any of the possible regions which
    # contains at least one point of the trajectory.
    for region in possible_regions:
        region_is_valid = False
        for j, polygon in enumerate(get_region_polygons(region)):
            if region_is_valid:
                break
            for i in range(len(lon)):
                point = Point(lon[i], lat[i])
                if polygon.contains(point):
                    region_is_valid = True
                    valid_regions.append(region)
                    break
    return valid_regions
