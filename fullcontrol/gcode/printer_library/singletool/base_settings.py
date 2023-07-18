default_initial_settings = {
    "print_speed": 1000,
    "travel_speed": 8000,
    "area_model": "rectangle",
    "extrusion_width": 0.4,
    "extrusion_height": 0.2,
    "nozzle_temp": 210,
    "bed_temp": 60,
    "fan_percent": 100,
    "print_speed_percent": 100,
    "material_flow_percent": 100,
    "e_units": "mm",
    "relative_e": True,
    "dia_feed": 1.75,
    "primer": "front_lines_then_y",
    "printer_command_list": {
        "home": "G28 ; home axes",
        "retract": "G10 ; retract",
        "unretract": "G11 ; unretract",
        "absolute_coords": "G90 ; absolute coordinates",
        "relative_coords": "G91 ; absolute coordinates",
        "units_mm": "G21 ; set units to millimeters",
        "mesh_bed_probe": '; Enable Mesh Compensation\nG29 S1 P"heightmap.csv"\nM376 H3'
    }
}
