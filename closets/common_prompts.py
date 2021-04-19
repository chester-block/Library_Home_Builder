from ..pc_lib import pc_types, pc_unit, pc_utils

def add_front_prompts(assembly):
    assembly.add_prompt("Front Thickness",'DISTANCE',pc_unit.inch(.75))
    assembly.add_prompt("Turn Off Pulls",'CHECKBOX',False)

def add_door_prompts(assembly):
    door_swing = assembly.add_prompt("Door Swing",'COMBOBOX',0,["Left","Right","Double"])
    door_swing.combobox_columns = 3
    assembly.add_prompt("Door Rotation",'ANGLE',120)
    assembly.add_prompt("Open Door",'PERCENTAGE',0)

def add_drawer_prompts(assembly):
    assembly.add_prompt("Open Drawer",'PERCENTAGE',0)

def add_front_overlay_prompts(assembly):
    assembly.add_prompt("Inset Front",'CHECKBOX',False)
    assembly.add_prompt("Door to Cabinet Gap",'DISTANCE',pc_unit.inch(.125))    
    assembly.add_prompt("Half Overlay Top",'CHECKBOX',True)
    assembly.add_prompt("Half Overlay Bottom",'CHECKBOX',True)
    assembly.add_prompt("Half Overlay Left",'CHECKBOX',True)
    assembly.add_prompt("Half Overlay Right",'CHECKBOX',True)
    assembly.add_prompt("Inset Reveal",'DISTANCE',pc_unit.inch(.125))
    assembly.add_prompt("Top Reveal",'DISTANCE',pc_unit.inch(.0625))
    assembly.add_prompt("Bottom Reveal",'DISTANCE',pc_unit.inch(0))
    assembly.add_prompt("Left Reveal",'DISTANCE',pc_unit.inch(.0625))
    assembly.add_prompt("Right Reveal",'DISTANCE',pc_unit.inch(.0625))
    assembly.add_prompt("Vertical Gap",'DISTANCE',pc_unit.inch(.125))
    assembly.add_prompt("Horizontal Gap",'DISTANCE',pc_unit.inch(.125))