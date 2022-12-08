extends Spatial

signal pressed
signal unpressed
# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var is_pressed = false
var in_area = false


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if in_area and Input.is_action_just_pressed("Interaction") and !is_pressed:
		is_pressed = true
		var newMaterial = SpatialMaterial.new() #Make a new Spatial Material
		newMaterial.albedo_color = Color(0, 1, 0, 1.0) #Set color of new material
		$"MeshInstance".material_override = newMaterial# Replace with function body.
		emit_signal("pressed")
	elif in_area and Input.is_action_just_pressed("Interaction") and is_pressed:
		is_pressed = false
		var newMaterial = SpatialMaterial.new() #Make a new Spatial Material
		newMaterial.albedo_color = Color(1, 0, 0, 1.0) #Set color of new material
		$"MeshInstance".material_override = newMaterial# Replace with function body. # Replace with function body.
		emit_signal("unpressed")



func _on_Area_body_entered(body):
	in_area = true
	
func _on_Area_body_exited(body):
	in_area = false
