extends Node

signal retry

func _ready():
	$PauseMenu.hide()

func _input(event):
	if event.is_action_pressed("pause"):
		var new_pause_state = not get_tree().paused 
		get_tree().paused = new_pause_state
		$PauseMenu.visible = new_pause_state


func _on_Menu_pressed():
	get_tree().paused = false # unpause before loading menu
	get_tree().change_scene("res://UIcomponents/Menu.tscn")


func _on_Retry_pressed():
	get_tree().paused = false # Unpause before reloading scene :)
	get_tree().reload_current_scene()
	#emit_signal("retry")


func _on_Continue_pressed():
	var new_pause_state = not get_tree().paused 
	get_tree().paused = new_pause_state
	$PauseMenu.visible = new_pause_state
