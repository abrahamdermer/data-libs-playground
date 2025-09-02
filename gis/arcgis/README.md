# ArcGIS / ArcPy (Notes)

ArcGIS is a commercial GIS platform. `arcpy` requires ArcGIS Pro/ArcMap installed.
This repo provides notes and pseudo-code only (no runtime here).

## Common tasks
- Listing layers, exporting map to image/PDF
- Geoprocessing tools (buffer, clip, intersect)

## Example (pseudo-code)
```python
# import arcpy
# arcpy.env.workspace = r"C:\GIS\project.gdb"
# arcpy.Buffer_analysis("roads", "roads_buffer_100m", "100 meters")
```

> Tip: Prefer GeoPandas/Shapely for open-source pipelines when ArcGIS isn't available.
