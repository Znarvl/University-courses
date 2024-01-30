extends Node

func _physics_process(delta):
	if $Player.get_global_translation()[1] < -80:
		get_tree().reload_current_scene()

func _on_PressurePlate_pressed():
		$LevelLogic/Door.open() # Replace with function body.


func _on_PressurePlate_unpressed():
		$LevelLogic/Door.close() # Replace with function body.


func _on_PressurePlate2_pressed():
		$LevelLogic/Door2.open()


func _on_PressurePlate2_unpressed():
		$LevelLogic/Door2.close()


func _on_PressurePlate3_pressed():
		$LevelLogic/Door3.open()


func _on_PressurePlate3_unpressed():
		$LevelLogic/Door3.close()


func _on_Door_crushed():
	get_tree().reload_current_scene()

func _on_OpenFinalDoorArea_body_entered(body):
	var newMaterial = SpatialMaterial.new()
	newMaterial.proximity_fade_enable = true
	newMaterial.proximity_fade_distance = 22
	$World/TransparentExitWall/MeshInstance.material_override = newMaterial
	$LevelLogic/ExitDoor.open()


func _on_LevelCompleteArea_body_entered(body):
	if body.name == "Player":
		print("oops")
		get_tree().change_scene("res://Levels/Level3.tscn")


func _on_PauseMenu_retry():
	get_tree().reload_current_scene()
