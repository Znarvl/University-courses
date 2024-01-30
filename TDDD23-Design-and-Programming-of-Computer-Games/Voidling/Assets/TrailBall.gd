extends Spatial

func _ready():
	var anim = $AnimationPlayer.get_animation("existing")
	anim.set_loop(true)
	$AnimationPlayer.play("existing")

