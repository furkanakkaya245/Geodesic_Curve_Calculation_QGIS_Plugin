# QGIS Geodesic Curve Calculator Plugin

This plugin is a specialized tool developed for **Geodetic and Geomatics Engineering** applications. It enables users to compute and visualize geodesic curves (the shortest path between two points on an ellipsoid) within the QGIS environment.

## Key Features
* **Ellipsoidal Precision:** Unlike standard Euclidean geometry, this plugin computes the shortest path based on the Earth's curvature using the **WGS84 ellipsoid**.
* **Direct and Inverse Solutions:** Solves the inverse geodetic problem to find distances and azimuths, and the direct problem to generate intermediate points for the curve.
* **Automated Visualization:** Automatically generates a vector line layer (Temporary Scratch Layer) representing the geodesic curve.
* **Metric Accuracy:** Implements **Vincenty's formulae**, providing high numerical stability and millimeter-level accuracy for global distances.

## Scientific Methodology
The plugin bridges the gap between raw geodetic algorithms and spatial visualization. By leveraging Python's computational power and QGIS's rendering engine, it allows for:
1.  **Coordinate Input:** Real-time entry of Latitude and Longitude.
2.  **Densification:** The geodesic curve is not just a straight line; it is a densified series of points following the ellipsoidal path.
3.  **Validation:** Essential for validating manual adjustment calculations performed in external scripts.

## Installation & Usage
1.  Place the `Geodesic_Curve_Calculator` directory into your QGIS plugins folder.
2.  Activate the plugin via **Plugins > Manage and Install Plugins**.
3.  Input the start and end coordinates and click **Calculate** to see the curve on the map.

## Academic Context
This tool was developed as part of a comprehensive geodetic study, focusing on the integration of Least Squares Adjustment (LSA) and spatial data analysis.
