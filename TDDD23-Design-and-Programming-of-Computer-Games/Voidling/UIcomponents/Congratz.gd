extends Control



func _on_StartButton_pressed():
	get_tree().change_scene("res://UIcomponents/Menu.tscn")


func _on_Quit_pressed():
	get_tree().quit()
