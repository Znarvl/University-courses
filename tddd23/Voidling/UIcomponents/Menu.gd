extends Control


func _ready():
	pass # Replace with function body.


func _on_StartButton_pressed():
	$MainMenu.hide()
	$ChooseLevel.show()


func _on_Quit_pressed():
	get_tree().quit()

