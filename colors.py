import re, shutil

# Function to replace colors in a file
def replace_colors_in_file(file_path, color_map):
    # Open the file for reading
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Iterate over the color map and replace all occurrences of each color
    for old_color, new_color in color_map.items():
        # Use regex to find all instances of the old color and replace with the new color
        file_content = re.sub(re.escape(old_color), new_color, file_content, flags=re.IGNORECASE)

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(file_content)
    print(f"Replaced colors in {file_path}")

# Example color mapping (you can use the dictionary from the previous response)
color_map = {
    "#FFC107": "#0745FF",
    "#FFD333": "#1d528b",
    "#FFC800": "#0037FF",
    "#E6B400": "#0032E6",
    "#FFEFB3": "#B3C3FF",
    "#FFCB0D": "#0D40FF",
    "#F2BE00": "#0033F2",
    "#E8A800": "#003FE8",
    "#D39E00": "#0035D3",
    "#C69500": "#0030C6"
}

# Specify the path to your file
orig_path = 'static/css/style old.css'
file_path = 'static/css/style.css'
shutil.copy(orig_path, file_path)

# Call the function to replace colors
replace_colors_in_file(file_path, color_map)
