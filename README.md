# geostuff


need:
visual c++ build tool: https://stackoverflow.com/questions/48541801/microsoft-visual-c-14-0-is-required-get-it-with-microsoft-visual-c-build-t#49984619

(see https://stackoverflow.com/questions/48541801/microsoft-visual-c-14-0-is-required-get-it-with-microsoft-visual-c-build-t#49984619)

osgeo4w (with gdal 204, to add in ..\venv64\Lib\site-packages\django\contrib\gis\gdal\libgdal.py )

postgis

If Project is throwing a "GDALException at /steps/ OGR failure." check console's log, gcs.csv may be missing in gdal directory. You can copy paste it from epsg_csv directory