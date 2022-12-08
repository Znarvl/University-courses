extends Node

func _physics_process(delta):
	if $Player.get_global_translation()[1] < -80:
		get_tree().reload_current_scene()

func _on_PressurePlate_pressed():
	$LevelLogic/Door.open()


func _on_PressurePlate_unpressed():
	$LevelLogic/Door.close()


func _on_LevelCompleteArea_body_entered(body):
	if body.name == "Player":
		print("oops")
		get_tree().change_scene("res://Levels/Level2.tscn")
	

func _on_Door_crushed():
	print("hej")
	get_tree().reload_current_scene()


func _on_PauseMenu_retry():
	get_tree().reload_current_scene()
