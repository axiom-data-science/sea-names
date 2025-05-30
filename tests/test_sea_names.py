#!/usr/bin/env pytest
"""Test case for sea names."""
import pytest

import sea_names


@pytest.mark.slow
def test_sea_name():
    """Test that we can determine the sea name from these points."""

    test_cases = {
        "Adriatic Sea": [
            (15.522, 43.195),
        ],
        "Aegean Sea": [
            (25.31, 38.582),
        ],
        "Alboran Sea": [
            (-3.33, 36.13),
        ],
        "Andaman Sea": [
            (96.00, 11.03),
        ],
        "Baltic Sea": [
            (20.08, 58.32),
        ],
        "Coastal Waters of Mississippi": [
            (-88.87, 30.30),
        ],
        "English Channel": [
            (-1.38, 50.14),
        ],
        "Gulf of Aqba": [
            (34.74, 28.83),
        ],
        "Gulf of St Lawrence": [
            (-58.85, 50.11),
        ],
        "Inner Seas off West Coast of Scotland": [
            (-6.98, 57.12),
        ],
        "Lake Erie": [
            (-81.65, 41.98),
        ],
        "Mediterranean Sea": [
            (-5.62, 35.95),
        ],
        "Norwegian Sea": [
            (3.15, 69.75),
        ],
        "Sea of Marmara": [
            (27.81, 40.79),
        ],
        "St. Lawrence River": [
            (-69.83, 47.68),
        ],
        # Three seas/regions with multiple bounding boxes with the same name
        "Bering Sea": [
            (166.857310, 58.484235),
            (-164.962849, 56.979633),
        ],
        "South Pacific Ocean": [
            (177.573269, -27.738784),
            (-153.422827, -28.822356),
        ],
        "North Pacific Ocean": [
            (174.584988, 24.149949),
            (-173.813451, 19.252229),
        ],
    }
    for sea_name, points in test_cases.items():
        for point in points:
            name = sea_names.get_sea_name(point)
            assert sea_name == name
