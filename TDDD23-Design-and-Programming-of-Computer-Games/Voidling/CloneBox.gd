extends KinematicBody


var box = null

var recording = false
var recording_iteration = 0
var replaying = false

var copied_movement = []
var copied_rotation = []

#replaying variables
var loop_iteration = 0
var loop_length = 0 

func _ready():
	pass

func set_box_to_record(b):
	box = b
	print("assignade böx")

func update_box():
	replay_movement()


func record_box_movement():
	copied_movement.append(box.get_global_translation())
	recording_iteration += 1

func enable_box():
	show()
	$CollisionShape.disabled = false
	
func disable_box():
	hide()
	$CollisionShape.disabled = true
	

func replay_movement():
	if loop_iteration == loop_length:
		loop_iteration = 0
		#reset_clone()
	set_position(loop_iteration)
	loop_iteration += 1;

func set_position(i): #sets position based on the loop iteration index
	var cord = Vector3(copied_movement[i][0], copied_movement[i][1], copied_movement[i][2])
	set_global_translation(cord)
	
func set_rotation(i):
	var rot


