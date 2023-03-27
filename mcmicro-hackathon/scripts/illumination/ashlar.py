import os
import spatialdata as sd
import shutil
import xarray as xr


def convert(tif_file: str, output_file: str):
    import dask_image.imread
    import xarray as xr

    x = dask_image.imread.imread(tif_file)
    print(x)
    x = x.squeeze(0)
    x = xr.DataArray(x, dims=["y", "x", "c"])
    x = x.transpose("c", "y", "x")

    sdata = sd.SpatialData(images={"img": x}, transformations={("/images/img", "global"): None})
    outfile = os.path.join(output_file, f"data.zarr")

    if os.path.isdir(outfile):
        shutil.rmtree(outfile)
    # the chunk size needs to be specified otherwise this operation requires a lot of memory
    sdata.write(outfile)