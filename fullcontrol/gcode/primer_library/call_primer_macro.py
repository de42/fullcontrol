
from fullcontrol.gcode import Point, Extruder
from fullcontrol.gcode import ManualGcode


def primer(end_point: Point) -> list:
    'returns an empty list for the primer steps. no primer is desired, but a list object is needed for consistency'
    primer_steps = []
    primer_steps.append(ManualGcode(text='M98 P"0:/macros/intro_line.g" ; Call Primer via Macro'))
    return primer_steps
