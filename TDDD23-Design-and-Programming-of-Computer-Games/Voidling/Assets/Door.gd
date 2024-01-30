extends Spatial

signal crushed

var is_open = false;

func open():
	is_open = true;
	$AnimationPlayer.play("Open")

func close():
	is_open = false;
	$AnimationPlayer.play("Close")


func _on_Area_body_entered(body):
	if !is_open:
		emit_signal("crushed")
