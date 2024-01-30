extends Sprite


var cloning = false
var has_cloned = false

# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _process(delta):
	if cloning:
		modulate.a8 = (250 + sin(OS.get_ticks_msec()/250.0) * 250)
	elif has_cloned:
		modulate.a8 = 500

	
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_Player_hud_cloning2():
	cloning = true
	has_cloned = false


func _on_Player_hud_not_cloning2():
	cloning = false # Replace with function body.
	has_cloned = true

