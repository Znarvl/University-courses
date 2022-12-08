extends Panel

var style = StyleBoxFlat.new()
var cloning = false
var has_cloned = false
var deleted_clone = false


func _ready():
	# The Panel doc tells you which style names there are
	add_stylebox_override("panel", style)
	set_process(true)

func _process(delta):
	var org_color = Color(100, 0, 0)
	style.set_bg_color(org_color)
	if cloning:
		var color = Color(0.5*sin(OS.get_ticks_msec()/100.0)+0.5, 0, 0)
		style.set_bg_color(color)
		# Don't forget to update so the control will redraw
	elif has_cloned:
		var color = Color(0, 100, 0)
		style.set_bg_color(color)
	update()# Replace with function body.
	
	
	
func _on_Player_hud_cloning2():
	deleted_clone = false
	cloning = true
	has_cloned = false

func _on_Player_hud_not_cloning2():
	deleted_clone = false
	cloning = false # Replace with function body.
	has_cloned = true

func _on_Player_deleted_clone():
	has_cloned = false
	cloning = false # Replace with function body.
	deleted_clone = true # Replace with function body.



