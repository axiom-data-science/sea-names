"""Unit tests for complex trajectory parsing."""
from pathlib import Path

import numpy as np
import pytest

from numpy.lib.npyio import NpzFile

from sea_names.geo import get_sea_names_for_trajectory


@pytest.fixture
def great_white_shark_data() -> NpzFile:
    """Fixture for the trajectory data of a reasonably sized deployment."""
    pth = Path(__file__).parent / "testdata/great-white-shark.npz"
    return np.load(pth)


@pytest.mark.slow
def test_get_sea_names_for_great_white_shark_data(great_white_shark_data):
    lon = great_white_shark_data["lon"]
    lat = great_white_shark_data["lat"]
    regions = get_sea_names_for_trajectory(lon, lat, chunk_size=len(lon))
    assert regions == ["Arctic Ocean", "Beaufort Sea", "Bering Sea", "Chukchi Sea"]
