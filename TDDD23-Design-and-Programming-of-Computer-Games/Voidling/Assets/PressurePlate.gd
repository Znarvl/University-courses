extends Spatial

signal pressed
signal unpressed


var numberOnPlate = 0 # keeps track of number of units on plate. Resolves an issue with signals
var is_pressed = false

func _ready():
	pass # Replace with function body.


func _on_Area_body_entered(body):
	numberOnPlate += 1
	if !is_pressed:
		emit_signal("pressed") #to avoid doing it all the time a body enters. Just the first time a body enters the plate :)
	is_pressed = true
	
	var newMaterial = SpatialMaterial.new() #Make a new Spatial Material
	newMaterial.albedo_color = Color(0, 1, 0, 1.0) #Set color of new material
	$"MeshInstance".material_override = newMaterial# Replace with function body.


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
