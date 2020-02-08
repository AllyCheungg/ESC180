import utilities

def rotate_90_degrees(image_array, direction = 1):
	#1 for clock_wise. -1 for anticlockwise
	rotated_image = []
		
	if direction == 1:
		for i in range(len(image_array)):
			row = []
			for j in range (len(image_array[0])-1,-1,-1):
				row.append(image_array[j][i])
			rotated_image.append(row)
		return rotated_image
	
	if direction == -1:
		for i in range(len(image_array)-1,-1,-1):
			row = []
			for j in range (len(image_array)):
				row.append(image_array[j][i])
			rotated_image.append(row)
		return rotated_image		


def flip_image(image_array, axis = 0):
	#axis = -1 (along x = y), 0 along y, 1 along x
	if axis == 0:
		for i in range(len(image_array)):
			image_array[i].reverse()
		return image_array
	
	elif axis == 1:
		output_array = []
		for r in range(len(image_array[0])):
			output_array.append([0 for a in range(len(image_array[r]))])		
		for i in range(len(image_array)):
			for j in range(len(image_array[0])):
				output_array[i][j] = image_array[len(image_array)-1-i][j]
		return output_array
	elif axis == -1:
		output_array = []
		for r in range(len(image_array[0])):
			output_array.append([0 for a in range(len(image_array[r]))])
		n= len(image_array)
		for i in range(len(image_array)):
			for j in range(len(image_array[0])):
				output_array[i][j] = image_array[-1-j][-1-i]
		return output_array
	
def crop(image_array, direction, n_pixels):
	
	#####################################
	##########YOUR CODE GOES HERE########
	#####################################
	#return output_array

'''
def rgb_to_grayscale(rgb_image_array):

	#####################################
	##########YOUR CODE GOES HERE########
	#####################################

	#return output_array

def invert_rgb(image_array):
	#####################################
	##########YOUR CODE GOES HERE########
	#####################################

	#return output_array
    
def gaussian_blur(image_array, sigma=0.84089):

	#####################################
	##########YOUR CODE GOES HERE########
	#####################################

	#return output_array

def image_to_drawing(image_array):
	#####################################
	##########YOUR CODE GOES HERE########
	#####################################

	#return output_array
'''

if (__name__ == "__main__"):
	file = 'robot.png'
	lists = flip_image(utilities.image_to_list(file),1)
	utilities.write_image(lists, 'new.png')

	#file = 'robot.png'
	#utilities.write_image(rgb_to_grayscale)
        #utilities.image_to_list(file)), 'gray.png')

