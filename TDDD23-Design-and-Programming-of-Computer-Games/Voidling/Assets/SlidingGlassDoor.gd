extends Spatial

func open_door():
	$AnimationPlayer.play("Open")
	
func close_door():
	$AnimationPlayer.play("Close")

