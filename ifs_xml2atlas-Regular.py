import xml.etree.ElementTree as ET
from PIL import Image
import os

def main():
    file_path = input("Enter the path to the XML file: ").strip().strip('"')
    raw_folder = os.path.basename(os.path.dirname(os.path.dirname(file_path)))
    parent_folder = raw_folder.removesuffix('_ifs')
    output_lines = []
    images = []

    output_subdir = f"{parent_folder}_atlas"
    run_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(run_dir, output_subdir)
    os.makedirs(output_folder, exist_ok=True)

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except Exception as e:
        msg = f"Error reading or parsing the file: {e}"
        print(msg)
        return

    for texture in root.findall('.//texture'):
        size_elem = texture.find('size')

        if size_elem is not None:
            try:
                width, height = map(int, size_elem.text.strip().split())
            except:
                width, height = 4096, 4096
        else:
            width, height = 4096, 4096

        for image in texture.findall('image'):
            name = image.attrib.get('name', 'Unnamed')

            uvrect = image.find('uvrect')
            imgrect = image.find('imgrect')

            if uvrect is not None and imgrect is not None:
                try:
                    uv_values = list(map(int, uvrect.text.strip().split()))
                    img_values = list(map(int, imgrect.text.strip().split()))

                    uv_div1 = uv_values[0] // 2
                    uv_div3 = uv_values[2] // 2

                    images.append((f"{name}.png", (uv_div1, uv_div3)))

                except Exception as e:
                    error_line = f"  Error parsing image '{name}': {e}"
                    print(error_line)
                    output_lines.append(error_line)

    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    img_dir = os.path.dirname(file_path)

    for filename, position in images:
        filepath = os.path.join(img_dir, filename)
        if not os.path.exists(filepath):
            print(f"Error: '{filename}' not found in '{img_dir}'.")
            return
        img = Image.open(filepath).convert("RGBA")
        canvas.paste(img, position, img)

    output_path = os.path.join(output_folder, "output.png")
    canvas.save(output_path)
    print(f"\n\nDone.\n\nAtlas saved as '{output_path}'")

if __name__ == "__main__":
    main()
