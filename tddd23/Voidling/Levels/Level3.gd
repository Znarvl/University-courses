extends Node

var uno = false
var dos = false
var tres = false

var yuh = false

func _physics_process(delta):
	if $Player.get_global_translation()[1] < -80:
		get_tree().reload_current_scene()
		
	if uno and dos and tres and !yuh:
		yuh = true
		$LevelLogic/ExitDoor.open()

func _on_PressurePlate_pressed():
	$LevelLogic/SlidingGlassDoor.open_door()


func _on_PressurePlate_unpressed():
	$LevelLogic/SlidingGlassDoor.close_door()


func _on_BoxPressurePlate_pressed():
	$LevelLogic/SlidingGlassDoor.open_door()


func _on_BoxPressurePlate_unpressed():
	$LevelLogic/SlidingGlassDoor.close_door()

func _on_LevelCompleteArea_body_entered(body):
	if body.name == "Player":
		print("oops")
		get_tree().change_scene("res://Levels/Level4.tscn")


func _on_PauseMenu_retry():
	get_tree().reload_current_scene()
 # Replace with function body.


func _on_Uno_pressed():
	uno = true


func _on_Uno_unpressed():
	uno = false
	if yuh:
		yuh = false
		$LevelLogic/ExitDoor.close()


func _on_Dos_pressed():
	dos = true


func _on_Dos_unpressed():
	dos = false
	if yuh:
		yuh = false
		$LevelLogic/ExitDoor.close()

func _on_Tres_pressed():
	tres = true


func _on_Tres_unpressed():
	tres = false
	if yuh:
		yuh = false
		$LevelLogic/ExitDoor.close()
