extends Node

var exit_is_pressed_1 = false

var exit_is_pressed_2 = false

func _physics_process(delta):
	if $Player.get_global_translation()[1] < -80:
		get_tree().reload_current_scene()

func _on_PressurePlate_pressed():
	$LevelLogic/Door.open() # Replace with function body.


func _on_PressurePlate_unpressed():
	$LevelLogic/Door.close() # Replace with function body.


func _on_PressurePlate2_pressed():
	$LevelLogic/Door3.open()


func _on_PressurePlate2_unpressed():
	$LevelLogic/Door3.close()


func _on_PressurePlate3_pressed():
	$LevelLogic/Door4.open()
	$LevelLogic/Door.close()  # Replace with function body.


func _on_PressurePlate3_unpressed():
	$LevelLogic/Door4.close()
	$LevelLogic/Door.open() # Replace with function body. # Replace with function body. # Replace with function body.


func _on_BoxPressurePlate2_pressed():
	 exit_is_pressed_1 = true
	 $LevelLogic/Door2.open() # Replace with function body.


func _on_BoxPressurePlate2_unpressed():
	exit_is_pressed_1 = false
	$LevelLogic/Door2.close() # Replace with function body.
	


func _on_BoxPressurePlate_pressed():
	if exit_is_pressed_1:
		$LevelLogic/ExitDoor.open()
		


func _on_LevelCompleteArea_body_entered(body):
		if body.name == "Player":
			print("ooof")
			get_tree().change_scene("res://Levels/Level6.tscn") # Replace with function body.


func _on_PauseMenu_retry():
	get_tree().reload_current_scene()
 # Replace with function body.
