extends Node2D

var cloning = false
var has_cloned = false

func _process(delta):
	if cloning:
		modulate.a8 = (250 + sin(OS.get_ticks_msec()/250.0) * 250)
	elif has_cloned:
		modulate.a8 = 500

	
	


func _on_Player_hud_cloning1():
	cloning = true
	has_cloned = false



func _on_Player_hud_not_cloning1():
	cloning = false # Replace with function body.
	has_cloned = true

