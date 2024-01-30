extends Node

var pillar_rotated = false


func _ready():
	$Player.set_wide_fov()
	
	
func _physics_process(delta):
	if $Player.get_global_translation()[1] < -80:
		get_tree().reload_current_scene()


func _on_SectionPlate_pressed():
	pillar_rotated = true
	$AnimationPlayer.play("RotateSectionActive")


func _on_SectionPlate_unpressed():
	pillar_rotated = false
	$AnimationPlayer.play("RotateSectionDisable")

func _on_BigPressurePlate_pressed():
	$AnimationPlayer.play("RotateSection2Active")
	
func _on_BigPressurePlate_unpressed():
	$AnimationPlayer.play("RotateSection2Disable")

func _on_BigPressurePlate2_pressed():
	$AnimationPlayer.play("RotateSectionActive")

func _on_BigPressurePlate2_unpressed():
	$AnimationPlayer.play("RotateSectionDisable")


func _on_BigPressurePlate4_pressed():
	$AnimationPlayer.play("RotateSection2Active")


func _on_BigPressurePlate4_unpressed():
	$AnimationPlayer.play("RotateSection2Disable")








func _on_ExitBoxPressurePlate_pressed():
	$LevelLogic/ExitDoor.open()


func _on_BigPressurePlate3_pressed():
	$LevelLogic/SlidingGlassDoor.open_door()


func _on_LevelCompleteArea_body_entered(body):
		if body.name == "Player":
			get_tree().change_scene("res://Levels/Level7.tscn")
