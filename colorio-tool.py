import colorio
import math
from tabulate import tabulate

def jch_to_lab(jch):
	in_lightness, in_chroma, in_hue = jch

	a_coord = in_chroma * (math.cos(math.radians(in_hue)))
	b_coord = in_chroma * (math.sin(math.radians(in_hue)))

	jab = [in_lightness, a_coord, b_coord]
	
	return jab

def prompt_jch_to_ciecam16ucs():
	L_A = 64 / math.pi / 5
	cam16ucs = colorio.cs.CAM16UCS(0.69, 20, L_A)

	in_lightness = int(input("J (Lightness): "))
	in_chroma = int(input("c (Chroma): "))
	in_hue = int(input("h (Hue): "))

	in_jch = [in_lightness, in_chroma, in_hue]

	print(cam16ucs.to_rgb255(jch_to_lab(in_jch)))

def jch_diff(jch1, jch2):
	jab1 = jch_to_lab(jch1)
	jab2 = jch_to_lab(jch2)

	diff = jab_diff(jab1, jab2)

	return diff

def jab_diff(jab1, jab2):
	in_j1, in_a1, in_b1 = jab1
	in_j2, in_a2, in_b2 = jab2

	diff = math.sqrt((in_j2 - in_j1)**2 + (in_a2 - in_a1)**2 + (in_b2 - in_b1)**2)

	return diff

def prompt_color_diff():
	option = input("Jch or Jab input?\n\t1. Jch\n\t2. Jab\n")
	print("")

	in_j1 = int(input("J1: "))
	if option == "1":
		in_1_1 = float(input("c1: "))
		in_2_1 = float(input("h1: "))
	elif option == "2":
		in_1_1 = float(input("a1: "))
		in_2_1 = float(input("b1: "))
	color1 = [in_j1, in_1_1, in_2_1]

	in_j2 = int(input("J2: "))
	if option == "1":
		in_1_2 = float(input("c2: "))
		in_2_2 = float(input("h2: "))
	elif option == "2":
		in_1_2 = float(input("a2: "))
		in_2_2 = float(input("b2: "))
	color2 = [in_j2, in_1_2, in_2_2]

	if option == "1":
		print(jch_diff(color1, color2))
	elif option == "2":
		print(jab_diff(color1, color2))

def generate_palette():
	L_A = 64 / math.pi / 5
	cam16ucs = colorio.cs.CAM16UCS(0.69, 20, L_A)

	grey_range       = int(input("# of Greys: "))
    if (grey_range > 0):
	    min_lightness    = float(input("Greys min J: "))
	    max_lightness    = float(input("Greys max J: "))
	accent_range     = int(input("# of Accents: "))
    if (accent_range > 0):
	    accent_lightness = float(input("Accents J: "))
	    accent_chroma    = float(input("Accents c: "))
	
    table_result     = [["Name", "J", "h", "R", "G", "B", "a*", "b*"]]

	for g in range(grey_range):
		current_lightness = (max_lightness - min_lightness) / (grey_range - 1) * g + min_lightness
		derived_jch       = [current_lightness, 0, 0]
		result            = cam16ucs.to_rgb255(jch_to_lab(derived_jch))
		result_r          = result[0]
		result_g          = result[1]
		result_b          = result[2]
		current_row       = ["grey" + str(g),
                             round(current_lightness,3),
                             round(0.000,3),
                             round(result_r,3),
                             round(result_g,3),
                             round(result_b,3),
                             round(0.000,3),
                             round(0.000,3)]
		table_result.append(current_row)

		# Old method of printing results
		#print("[grey" + str(g) + "]")
		#print("Lightness: " + str(round(current_lightness,3)))
		#print("r: " + str(round(result_r,3)) + " " +
		#      "g: " + str(round(result_g,3)) + " " +
		#      "b: " + str(round(result_b,3)) + " ")
	
	for a in range(accent_range):
		current_hue = (360 / accent_range) * a + (360 / accent_range / 2)
		derived_jch = [accent_lightness, accent_chroma, current_hue]
		result      = cam16ucs.to_rgb255(jch_to_lab(derived_jch))
		result_r    = result[0]
		result_g    = result[1]
		result_b    = result[2]
		result_x    = accent_chroma * math.cos(math.radians(current_hue))
		result_y    = accent_chroma * math.sin(math.radians(current_hue))
		current_row = ["accent" + str(a),
                       round(accent_lightness,3),
                       round(current_hue,3),
                       round(result_r,3),
                       round(result_g,3),
                       round(result_b,3),
                       round(result_x,3),
                       round(result_y,3)]
		table_result.append(current_row)

		# Old method of printing results
		#print("[accent" + str(a) + "]")
		#print("Hue: " + str(round(current_hue,3)))
		#print("r: " + str(round(result_r,3)) + " " +
		#      "g: " + str(round(result_g,3)) + " " +
		#      "b: " + str(round(result_b,3)) + " ")
	
	print(tabulate(table_result,headers="firstrow"))

def prompt_menu():
	option = ""

	while option != "0":
		option = input("\nChoose from the options available:\n\t1. Generate Palette\n\t2. Get from Jch\n\t3. Color diff\n")

		if option == "1":
			generate_palette()
		elif option == "2":
			prompt_jch_to_ciecam16ucs()
		elif option == "3":
			prompt_color_diff()
		else:
			print("Invalid option, exiting...")
			option = "0"

prompt_menu()
