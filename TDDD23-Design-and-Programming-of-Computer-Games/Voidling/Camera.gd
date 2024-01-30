extends Camera

var target
export var smooth_speed: float
export var offset: Vector3
var lerp_speed = 10


func _ready():
	target = get_parent()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _physics_process(delta):
	if(target != null):
		#global_transform = target.global_transform.interpolate_with(global_transform, lerp_speed * delta)
		self.translation = lerp(self.translation, target.translation + offset, smooth_speed * delta)
