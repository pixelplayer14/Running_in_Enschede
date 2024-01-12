import json
with open("dataV2/export.geojson","r") as original_file:
    with open("dataV2/minimized/export_min.geojson","w") as minimized_file:
        original_json = json.load(original_file)
        minimized_json = {
            "type": "FeatureCollection",
            "generator": "overpass-turbo",
            "copyright": "The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.",
            "timestamp": "2023-12-24T11:30:45Z",
            "features": []}
        for feature in original_json["features"]:
            minimized_json["features"].append({"type":"Feature","geometry":feature["geometry"]})
        json.dump(minimized_json,minimized_file)