extends VBoxContainer


func _ready():
	hide()


func _on_Level1_pressed():
	get_tree().change_scene("res://Levels/Level1.tscn")


func _on_Level2_pressed():
	get_tree().change_scene("res://Levels/Level2.tscn")

func _on_Level3_pressed():
	get_tree().change_scene("res://Levels/Level3.tscn")

func _on_Level4_pressed():
	get_tree().change_scene("res://Levels/Level4.tscn")
	
func _on_Level5_pressed():
	get_tree().change_scene("res://Levels/Level8.tscn")

func _on_Level6_pressed():
	get_tree().change_scene("res://Levels/Level5.tscn")

func _on_Level7_pressed():
	get_tree().change_scene("res://Levels/Level6.tscn")


func _on_Level8_pressed():
	get_tree().change_scene("res://Levels/Level7.tscn")


func _on_Back_pressed():
	hide()
	get_parent().get_node("MainMenu").show()












