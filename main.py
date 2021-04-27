import gdstk

# The GDSII file is called a library, which contains multiple cells.
lib = gdstk.Library()

# Geometry must be placed in cells.
cell = lib.new_cell("FIRST")

# Create the geometry (a single rectangle) and add it to the cell.
rect = gdstk.rectangle((0, 0), (2, 1))
cell.add(rect)

# Save the library in a GDSII or OASIS file.
lib.write_gds("first.gds")
lib.write_oas("first.oas")

# Optionally, save an image of the cell as SVG.
cell.write_svg("first.svg")
