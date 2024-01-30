extends Node


# Declare member variables here. Examples:
# var a = 2
# var b = "text"

func _physics_process(delta):
	if $Player.get_global_translation()[1] < -80:
		get_tree().reload_current_scene()

# Called when the node enters the scene tree for the first time.
func _ready():
	$Player.set_wide_fov() # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_LevelCompleteArea_body_entered(body):
	if body.name == "Player":
		get_tree().change_scene("res://Levels/Level8.tscn") # Replace with function body.


func _on_OpenFinalDoorArea_body_entered(body):
	$LevelLogic/ExitDoor.open() # Replace with function body.


func _on_PauseMenu_retry():
	get_tree().reload_current_scene()
 # Replace with function body.

