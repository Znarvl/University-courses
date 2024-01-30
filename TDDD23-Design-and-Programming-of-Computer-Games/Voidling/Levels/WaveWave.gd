extends Spatial

onready var wave1 = $Wave1

var waves = []
var waves_curr_translation = []

var t
var target


func _ready():
	t = 0.0
	waves.append($Wave1); 
	waves_curr_translation.clear()
	for w in waves:
		waves_curr_translation.append(w.get_global_translation())
	target = wave1.get_global_translation()#just a little hack
	
	
func shift_to_pillar1():
	t = 0.0
	target = $Pillar1.get_global_translation()
	waves_curr_translation.clear()
	for w in waves:
		waves_curr_translation.append(w.get_global_translation())
	
func shift_to_pillar2():
	t = 0.0
	target = $Pillar2.get_global_translation()
	waves_curr_translation.clear()
	for w in waves:
		waves_curr_translation.append(w.get_global_translation())
	
func shift_to_pillar3():
	t = 0.0
	target = $Pillar3.get_global_translation()
	waves_curr_translation.clear()
	for w in waves:
		waves_curr_translation.append(w.get_global_translation())
	
func shift_to_pillar4():
	t = 0.0
	target = $Pillar4.get_global_translation()
	waves_curr_translation.clear()
	for w in waves:
		waves_curr_translation.append(w.get_global_translation())
	
func _physics_process(delta):
	t += delta * 0.4
	if t > 1:
		t = 1
	for i in range(waves.size()):
		#waves[i].translation.x = waves_curr_translation[i].linear_interpolate(target, t).x #to get them to just move on the x axis
		var grr = waves[i].get_global_translation()
		var ex = waves_curr_translation[i].linear_interpolate(target, t).x
		grr.x = ex
		waves[i].set_global_translation(grr)
		


func _on_Pillar1Pressure_pressed():
	shift_to_pillar1()


func _on_Pillar2Pressure_pressed():
	shift_to_pillar2()


func _on_Pillar3Pressure_pressed():
	shift_to_pillar3()


func _on_Pillar4Pressure_pressed():
	shift_to_pillar4()
