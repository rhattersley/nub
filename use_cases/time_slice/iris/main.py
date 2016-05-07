from nub import timeit

import iris
from iris.time import PartialDateTime


# Create 5 years of hourly data => ~45k data points
# Similar to: http://hydromet-thredds.princeton.edu:9000/thredds/dodsC/MonitoringStations/butler.nc
def setup():
    from iris.coords import DimCoord
    from iris.cube import Cube
    import numpy as np
    times = np.arange(1299002400, 1462554000, 3600, dtype='f8')
    time = DimCoord(times, 'time', units='seconds since 1970-01-01')
    data = np.random.random(len(times))
    cube = Cube(data, dim_coords_and_dims=[(time, 0)])
    return cube


if __name__ == '__main__':
    cube = setup()

    iris.FUTURE.cell_datetime_objects = True

    with timeit('Extract month'):
        start = PartialDateTime(year=2016, month=1)
        end = PartialDateTime(year=2016, month=2)
        month = iris.Constraint(time=lambda cell: start <= cell < end)
        a_month = cube.extract(month)

    with timeit('Extract week'):
        start = PartialDateTime(year=2015, month=7, day=6)
        end = PartialDateTime(year=2015, month=7, day=13)
        week = iris.Constraint(time=lambda cell: start <= cell < end)
        a_week = cube.extract(week)
