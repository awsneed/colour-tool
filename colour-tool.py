import colour
import math
import tabulate

def polar_to_cartesian(jmh):
    lightness = jmh[0]
    color = jmh[1]
    hue = jmh[2]
    a = color * (math.cos(math.radians(hue)))
    b = color * (math.sin(math.radians(hue)))

    return [lightness, a, b]

def cam16ucs_jmh_to_srgb(jmh):
    out_rgb = colour.convert(polar_to_cartesian(jmh), "CAM16UCS", "sRGB")

    return [i * 255 for i in out_rgb]
    
def prompt_cam16ucs_jmh_to_srgb():
    in_j = int(input("Lightness: "))
    in_m = int(input("Colorfulness: "))
    in_h = int(input("Hue: "))

    print(cam16ucs_jmh_to_srgb([in_j, in_m, in_h]))

def generate_palette():
    grey_range       = int(input("# of Greys: "))
    if (grey_range > 0):
        min_lightness    = float(input("Greys min lightness: "))
        max_lightness    = float(input("Greys max lightness: "))

    accent_range     = int(input("# of Accents: "))
    if (accent_range > 0):
        hue_offset    = input("Custom hue offset: ")
        if (hue_offset == ""):
            hue_offset = (360 / accent_range / 2)
        else:
            hue_offset = float(hue_offset)
        accent_lightness = float(input("Accents lightness: "))
        accent_colorfulness    = float(input("Accents colorfulness: "))
    
    table_result     = [["Name", "J", "h", "R", "G", "B"]]

    for g in range(grey_range):
        current_lightness = (max_lightness - min_lightness) / (grey_range - 1) * g + min_lightness
        derived_jmh       = [current_lightness, 0, 0]
        result            = cam16ucs_jmh_to_srgb(derived_jmh)
        result_r          = result[0]
        result_g          = result[1]
        result_b          = result[2]
        current_row       = ["grey" + str(g),
                             round(current_lightness,3),
                             round(0.000,3),
                             round(result_r,3),
                             round(result_g,3),
                             round(result_b,3)]
        table_result.append(current_row)

        # Old method of printing results
        #print("[grey" + str(g) + "]")
        #print("Lightness: " + str(round(current_lightness,3)))
        #print("r: " + str(round(result_r,3)) + " " +
        #      "g: " + str(round(result_g,3)) + " " +
        #      "b: " + str(round(result_b,3)) + " ")
    
    for a in range(accent_range):
        current_hue = ((360 / accent_range) * a + hue_offset) % 360
        derived_jmh = [accent_lightness, accent_colorfulness, current_hue]
        result      = cam16ucs_jmh_to_srgb(derived_jmh)
        result_r    = result[0]
        result_g    = result[1]
        result_b    = result[2]
        current_row = ["accent" + str(a),
                       round(accent_lightness,3),
                       round(current_hue,3),
                       round(result_r,3),
                       round(result_g,3),
                       round(result_b,3)]
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
        option = input("\nChoose from the options available:\n\t1. Generate Palette\n\t2. Get from JMh\n")

        if option == "1":
            generate_palette()
        elif option == "2":
            prompt_cam16ucs_jmh_to_srgb()
        else:
            print("Invalid option, exiting...")
            option = "0"

prompt_menu()
