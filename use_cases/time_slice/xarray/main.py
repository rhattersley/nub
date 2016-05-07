from nub import timeit

import xarray as xr


# Create 5 years of hourly data => ~45k data points
# Similar to: http://hydromet-thredds.princeton.edu:9000/thredds/dodsC/MonitoringStations/butler.nc
def setup():
    import numpy as np
    import pandas as pd
    times = pd.date_range('2011-03-01 18', '2016-05-06 16', freq='H')
    data = np.random.random(len(times))
    da = xr.DataArray(data, coords=[times], dims=['time'])
    return da


if __name__ == '__main__':
    da = setup()

    with timeit('Extract month'):
        a_month = da.sel(time='2016-01')

    with timeit('Extract week'):
        a_week = da.sel(time=slice('2015-07-06', '2015-07-13'))
