extends KinematicBody

var clone_scene = preload("res://ClonePro.tscn")

onready var clone = clone_scene.instance()
onready var clone2 = clone_scene.instance()

export var speed = 15
export var fall_acceleration = 75
export var jump_impulse = 25
export var bounce_impulse = 16

var anim_player

signal hud_cloning1
signal hud_not_cloning1
signal hud_cloning2
signal hud_not_cloning2

var velocity = Vector3.ZERO

var is_cloning1 = false;
var is_cloning2 = false;

var holding = 0
var box = null

var camera_mode = 0 

func _ready():
	create_clone_pro()
	anim_player = get_node("Pivot/3DGodotRobot/AnimationPlayer")
	$Camera.make_current()
	
func _physics_process(delta):
	var forward = $Camera.transform.basis.z.normalized()
	print(forward)
	move(delta)
	
	if Input.is_action_just_pressed("clone_toggle1"):
		if !is_cloning1: 
			is_cloning1 = true
			clone.start_recording()
			emit_signal("hud_cloning1")
		else:
			is_cloning1 = false
			clone.stop_recording()
			emit_signal("hud_not_cloning1")
	if Input.is_action_just_pressed("clone_toggle2"):
		if !is_cloning2: 
			is_cloning2 = true
			clone2.start_recording()
			emit_signal("hud_cloning2")
		else:
			is_cloning2 = false
			clone2.stop_recording()
			emit_signal("hud_not_cloning2")
	if Input.is_action_pressed("delete_clones"):
		clone.reset_clone()
		clone2.reset_clone()
		
	
	# Ground velocity
	
	
	
	
func assign_grabbing(type, b):
	if holding != 0:
		return false
	holding = type
	box = b
	return true
	
func deassign_grabbing():
	holding = 0
	box = null
	
func get_box():
	return box

	
func create_clone_pro():
	clone.init(self)
	add_child(clone)
	clone2.init(self)
	add_child(clone2)
	
	
#camera related funcs !!!!!
func reset_top_view_camera():
	if camera_mode != 0:
		camera_mode = 0
		$AnimationPlayer.play_backwards("SetTopView")


func set_wide_fov(): #103 fov
	if camera_mode != 0:
		camera_mode = 0
		$AnimationPlayer.play("ChangeToFarFov")
	
func set_top_view_camera():
	if camera_mode != 1:
		camera_mode = 1
		$AnimationPlayer.play("SetTopView")

	
	
	
func move(delta):
	var is_moving
	if camera_mode == 0:
		is_moving = move_mode1(delta)
	if camera_mode == 1:
		is_moving = move_mode2(delta)
	
	var anim_to_play = "Idle-loop"
	if holding == 1:
		anim_to_play = "Crouch"
	if is_moving and not holding == 1:
		anim_to_play = "Run-loop"
	var current_anim = anim_player.get_current_animation()
	if current_anim != anim_to_play:
		anim_player.play(anim_to_play)

	
func move_mode1(delta):
	var direction = Vector3.ZERO
	var is_moving = false
	if Input.is_action_pressed("back"):
		direction.z += 1
		direction.x += 1
	if Input.is_action_pressed("forward"):
		direction.z -= 1
		direction.x -= 1
	if Input.is_action_pressed("left"):
		direction.x -= 1
		direction.z += 1
	if Input.is_action_pressed("right"):
		direction.x += 1
		direction.z -= 1
	if direction != Vector3.ZERO:
		is_moving = true
		direction = direction.normalized()
		$Pivot.look_at(translation + -direction, Vector3.UP)
	if is_on_floor() and Input.is_action_just_pressed("jump"):
		velocity.y += jump_impulse
		
	velocity.x = direction.x * speed
	velocity.z = direction.z * speed
	# Vertical velocity
	velocity.y -= fall_acceleration * delta
	# Moving the character
	velocity = move_and_slide(velocity, Vector3.UP)
	return is_moving
	
func move_mode2(delta):
	var direction = Vector3.ZERO
	var is_moving = false
	if Input.is_action_pressed("back"):
		direction.z += 1
	if Input.is_action_pressed("forward"):
		direction.z -= 1
	if Input.is_action_pressed("left"):
		direction.x -= 1
	if Input.is_action_pressed("right"):
		direction.x += 1
	if direction != Vector3.ZERO:
		is_moving = true
		direction = direction.normalized()
		$Pivot.look_at(translation + -direction, Vector3.UP)
	if is_on_floor() and Input.is_action_just_pressed("jump"):
		velocity.y += jump_impulse
		
	velocity.x = direction.x * speed
	velocity.z = direction.z * speed
	# Vertical velocity
	velocity.y -= fall_acceleration * delta
	# Moving the character
	velocity = move_and_slide(velocity, Vector3.UP)
	return is_moving

