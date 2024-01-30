extends Spatial

signal pressed
signal unpressed

var numberOnPlate = 0 # keeps track of number of units on plate. Resolves an issue with signals
var is_pressed = false

#smoothbox variables
var t = 0.0
var yes = false
var box = null
var box_first_pos_translation = null
var box_first_pos_rotation = null

func _physics_process(delta):
	if yes:
		smooth_move_box_on_button(delta)
		if t > 0.9:
			yes = false #yes
	

func smooth_move_box_on_button(delta):
	t += delta * 1.2
	var pos = box_first_pos_translation.linear_interpolate($BoxPos.get_global_translation(), t)
	box.set_global_translation(pos)
	#var rot = box_first_pos_rotation.linear_interpolate($BoxPos.get_global_rotation(), t)
	#box.set_global_rotation(pos)
	
func set_smooth_move(body):
	box = body
	box_first_pos_translation = box.get_global_translation()
	box_first_pos_rotation = box.get_global_rotation()
	yes = true
	
func reset_smooth():
	t = 0.0
	yes = false
	box = null
	box_first_pos_translation = null
	box_first_pos_rotation = null

	

func _on_Area_body_entered(body):
	numberOnPlate += 1
	if !is_pressed:
		emit_signal("pressed") #to avoid doing it all the time a body enters. Just the first time a body enters the plate :)
	is_pressed = true
	
	var newMaterial = SpatialMaterial.new() #Make a new Spatial Material
	newMaterial.albedo_color = Color(0, 1, 0, 1.0) #Set color of new material
	$"MeshInstance".material_override = newMaterial# Replace with function body.
	#set_smooth_move(body)
	#body.set_global_translation($BoxPos.get_global_translation())

func _on_Area_body_exited(body):
	numberOnPlate -= 1
	if numberOnPlate == 0:
		is_pressed = false
	if numberOnPlate < 0:
		numberOnPlate = 0
		is_pressed = false
	
	if !is_pressed:
		var newMaterial = SpatialMaterial.new() #Make a new Spatial Material
		newMaterial.albedo_color = Color(1, 0, 0, 1.0) #Set color of new material
		$"MeshInstance".material_override = newMaterial# Replace with function body. # Replace with function body.
		emit_signal("unpressed")
		#reset_smooth()


