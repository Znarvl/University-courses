extends Node


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var exit_is_open = false

# Called when the node enters the scene tree for the first time.
func _ready():
	$LevelLogic/Door3.open()

func _physics_process(delta):
	if $Player.get_global_translation()[1] < -80:
		get_tree().reload_current_scene()


func _on_PressurePlate_pressed():
	$LevelLogic/Door.open()
	$LevelLogic/Door3.close()

func _on_PressurePlate_unpressed():
	$LevelLogic/Door.close()
	$LevelLogic/Door3.open()

func _on_BoxPressurePlate_pressed():
	$LevelLogic/Door2.open()


func _on_BoxPressurePlate_unpressed():
	$LevelLogic/Door2.close()


func _on_PressurePlate2_pressed():
	$LevelLogic/Door4.open()


func _on_PressurePlate2_unpressed():
	$LevelLogic/Door4.close()

func _on_PauseMenu_retry():
	get_tree().reload_current_scene()



func _on_OpenFinalDoorArea_body_entered(body):
	$LevelLogic/ExitDoor.open() # Replace with function body.


func _on_LevelCompleteArea_body_entered(body):
	if body.name == "Player":
		get_tree().change_scene("res://UIcomponents/Congratulation.tscn") 
