extends RigidBody

var grabbable = false
var is_grabbed = false
var body = null

var player = null
var player_grab_pivot = null

# Called when the node enters the scene tree for the first time.
func _ready():
	set_gravity_scale(20)
	get_node("ToolTip").visible = false
	var current_scene = get_tree().get_current_scene() #get the current scene!!!!! Pretty neato
	player = current_scene.get_node("Player")
	player_grab_pivot = current_scene.get_node("Player/GrabbedObjectPivot")

func _process(delta):
	if grabbable: 
		var pos = get_translation()
		var cam = get_tree().get_root().get_camera()
		var screen_pos = cam.unproject_position(pos)
		get_node("ToolTip").set_position(Vector2(screen_pos.x + 20, screen_pos.y - 60))	

func _physics_process(delta):
	if is_grabbed:
		var translation = player_grab_pivot.get_global_translation() #get the playerpivot world pos
		set_global_translation(translation) 
		if Input.is_action_just_pressed("grab"):
			deassign_from_player()
	elif grabbable: #when in grabbable range, check for when the grab button gets pressed
		if Input.is_action_just_pressed("grab"):
			assign_to_player(player_grab_pivot)

func _on_GrabbableArea_body_entered(body):
	if !is_grabbed:
		grabbable = true
		get_node("ToolTip").visible = true


func _on_GrabbableArea_body_exited(body):
	if !is_grabbed:
		grabbable = false
		get_node("ToolTip").visible = false
	
func assign_to_player(pivot):
	var is_grabbing = player.assign_grabbing(1, self)
	if is_grabbing:
		player_grab_pivot = pivot #the crate emits a signal to level that it has been grabbed and
	#player_grab_pivot.get_parent().assign_grabbing(1) #one represents a box
		is_grabbed = true #  the level connects it to the scenes player 
		get_node("ToolTip").visible = false
	
func deassign_from_player():
	#player_grab_pivot.get_parent().deassign_grabbing()

	player.deassign_grabbing()
	is_grabbed = false

	var direction = Vector3.UP * 40
	apply_central_impulse(direction)
	
