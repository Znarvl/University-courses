extends KinematicBody

var clone_box = preload("res://CloneBox.tscn").instance()
var trail_ball = preload("res://Assets/TrailBall.tscn")

var player = null

var recording = false
var recording_iteration = 0
var replaying = false

#copied movement for clone
var copied_movement = []
var copied_holding = []
var copied_box_first_interaction_frame = 0 # keep tracks of when to start replaying box movement
var copied_direction = [] 
#pathtrail variables
var trail_balls = [] #evenly spaced balls showing the path of the clone
var last_point = Vector3(0, 0, 0) 

#replaying variables
var loop_iteration = 0
var loop_length = 0
var last_holding = 0 # always have 0 on init as default. trust me it works :) 
var touched_box = false 

#active recording ghost trail
var delay = 120 #delay of 120 frames (2 sec)
var current_ghost_trail_frame = 0

func reset_clone(): #reset to beginning values
	set_global_translation(Vector3(0, -20, 0))
	copied_movement = []
	copied_holding = []
	copied_direction = []
	recording_iteration = 0
	loop_iteration = 0
	loop_length = 0
	last_holding = 0
	delay = 120
	current_ghost_trail_frame = 0
	recording = false
	replaying = false
	touched_box = false
	remove_objects_on_pivot()
	clear_trail()
	hide()

func start_recording():
	reset_clone() 
	show()
	$CollisionShape.disabled = true #it starts disabled
	recording = true
	add_bigger_trail_ball(player.get_node("PathTrailPivot").get_global_translation())
	update_trail()

func stop_recording():
	$CollisionShape.disabled = false #nu äre kollision pp de 
	var loop_iteration = 0
	loop_length = copied_movement.size()
	recording = false
	replaying = true
	add_bigger_trail_ball(player.get_node("PathTrailPivot").get_global_translation()) #add ending ball

func init(p):
	player = p
	
func _ready():
	hide() #start hidden to avoid overlapp
	
func _physics_process(delta):
	if recording:
		record_movement()
		#ghost_trail()
		update_trail()
	elif replaying:
		replay_movement()
	
func record_movement(): 
	var translation = player.get_global_translation()
	copied_movement.append(translation)
	copied_holding.append(player.holding)
	copied_direction.append(player.get_node("Pivot").get_global_rotation())
	recording_iteration += 1
	
func ghost_trail(): #when recording we want a ghost behind showing the clone that is about to be created
	if delay > 0:
		delay -= 1
		set_position(0)
		set_holding(0)
	else:
		var i = current_ghost_trail_frame
		set_position(i)
		set_holding(i)
		current_ghost_trail_frame += 1
		
func update_trail():
	var p_point = player.get_node("PathTrailPivot").get_global_translation()
	if last_point.distance_to(p_point) > 2:
		last_point = p_point
		add_trail_ball(p_point)
	
func add_bigger_trail_ball(point):
	last_point = point
	var scene = get_tree().get_current_scene()
	var ball = trail_ball.instance()
	scene.add_child(ball)
	ball.set_scale(Vector3(1.5, 1.5, 1.5)) #bit bigger 
	ball.set_global_translation(point)
	trail_balls.append(ball)

func add_trail_ball(point):
	var scene = get_tree().get_current_scene()
	var ball = trail_ball.instance()
	scene.add_child(ball)
	ball.set_global_translation(point)
	trail_balls.append(ball)
	
func clear_trail():
	for ball in trail_balls:
		ball.queue_free()
	trail_balls.clear()

func replay_movement():
	if loop_iteration == loop_length:
		loop_iteration = 0
		#reset_clone()
	set_position(loop_iteration)
	set_holding(loop_iteration)
	set_direction(loop_iteration)
	loop_iteration += 1;
	
	
func set_direction(i):
	var direction = copied_direction[i]
	set_global_rotation(direction)
	
func set_position(i): #sets position based on the loop iteration index
	var cord = Vector3(copied_movement[i][0], copied_movement[i][1], copied_movement[i][2])
	set_global_translation(cord)
	
func set_holding(i): #sets clone holding based on loop iteration i
	var holding = copied_holding[i] #current iteration holding value
	if last_holding == holding: #if the last one still holds true, do nothing
		return 
	if holding == 0:
		remove_objects_on_pivot()
	if holding == 1: #1 == box
		$GrabbedObjectPivot.add_child(clone_box)
	last_holding = holding
		
func remove_objects_on_pivot(): #removes all the children on the holding. Gotta be some other way to do this heh
	var node = $GrabbedObjectPivot
	for n in node.get_children():
		node.remove_child(n)
	


