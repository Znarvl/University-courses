extends Spatial

onready var player = get_parent().get_node("Player")

func _on_TopViewChange_body_entered(body):
	player.set_top_view_camera()
