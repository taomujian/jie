from PIL import Image
def flip_vertical(image_path, output_path):
	with Image.open(image_path) as image:
		flipped_image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
		flipped_image.save(output_path)

flip_vertical('021b62817d7f439aab5338ea63fe1b4b.jpg', 'result.jpg')