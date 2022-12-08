extends Node

func _physics_process(delta):
	if $Player.get_global_translation()[1] < -80:
		get_tree().reload_current_scene()

# Called when the node enters the scene tree for the first time.
func _ready():
	#$Player.set_wide_fov() # Replace with function body.
	$Player.set_wide_fov()
	$World2/Lights/FinishLight.hide()



func _on_EndLevel_body_entered(body):
	$World2/ExitDoor.open()
	$World2/Lights/FinishLight.show()


func _on_EndLelelele_body_entered(body):
	if body.name == "Player":
		get_tree().change_scene("res://Levels/Level5.tscn")
