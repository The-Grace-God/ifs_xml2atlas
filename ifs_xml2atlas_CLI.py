import xml.etree.ElementTree as ET
import os

def main():
    file_path = input("Enter the path to the XML file: ").strip().strip('"')
    raw_folder = os.path.basename(os.path.dirname(os.path.dirname(file_path)))
    parent_folder = raw_folder.removesuffix('_ifs')
    output_lines = []

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
                size_info = f"{width}x{height}"
                canvas_note = ""
            except Exception:
                width, height = 4096, 4096
                size_info = f"{width}x{height}"
                canvas_note = "(auto-generated due to parse error)"
        else:
            width, height = 4096, 4096
            size_info = f"{width}x{height}"
            canvas_note = "(auto-generated; no canvas size in XML)"

        header = f"░▒▓▒░│ {parent_folder} IFS IMAGE ATLAS DATA │░▒▓▒░\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\nCanvas size: ({size_info}) {canvas_note}"
        print(header)
        output_lines.append(header)

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
                    img_div1 = img_values[0] // 2
                    img_div3 = img_values[2] // 2

                    block = (
                        f"\nImage name: {name}\n"
                        f"uv_croping: (X,{uv_div1}, Y,{uv_div3})\n"
                        f"img_position: (X,{img_div1}, Y,{img_div3})\n"
                        f"⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
                        f"\n░▒▓▒░│ RAW DATA │░▒▓▒░\n"
                        f"⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
                        f"uvraw: ({uv_values[0]}, {uv_values[1]}, {uv_values[2]}, {uv_values[3]})\n"
                        f"imgraw: ({img_values[0]}, {img_values[1]}, {img_values[2]}, {img_values[3]})\n"
                    )
                    print(block)
                    output_lines.append(block)

                except Exception as e:
                    error_line = f"  Error parsing image '{name}': {e}"
                    print(error_line)
                    output_lines.append(error_line)

    output_path = os.path.join(output_folder, f"{parent_folder}_Atlas_Data.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print(f"\nOutput also saved to '{output_path}'.")


if __name__ == "__main__":
    main()
