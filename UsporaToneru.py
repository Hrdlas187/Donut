import os
from PIL import Image

def invert_colors(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    pic_counter = 0
    output_subfolder = os.path.join(output_folder, "conv_output")
    os.makedirs(output_subfolder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path).convert('RGB')
            pixels = img.load()
            for y in range(img.height):
                for x in range(img.width):
                    r, g, b = pixels[x, y]
                    pixels[x, y] = (255 - r, 255 - g, 255 - b)
            
            base_name, ext = os.path.splitext(filename)
            new_filename = f"{base_name}_converted{ext}"
            
            output_path = os.path.join(output_subfolder, new_filename)
            img.save(output_path)
            
            pic_counter += 1
            print(f"Processed: {output_path}")

    
    if pic_counter == 0:
        print("Nebyly nalezeny zadne vyhovujici obrazky v definovane slozce.")
        input('Zmackni Enter.')
        exit()

print('\t __               ___               \n'
      '\t(_   _ _|_ ._ o    |  _  ._   _  ._ \n'
      '\t__) (/_ |_ |  |    | (_) | | (/_ |  \n'
      '\n\nZadnou z cest nezadavej s lomitkem na konci, nebo v uvozovkach!\n\n')


input_path = input("Zadej cestu ke slozce se screenshoty z osciloskopu:\nRETURN zvolí aktuální složku.\n> ")

if not input_path:
    input_path = os.path.dirname(os.path.abspath(__file__))
    
if not os.path.exists(input_path):
    raise FileNotFoundError(f"Cesta '{path}' neexistuje.")

print('\n\n')

output_path = input("Zadej cestu, na niz bude vytvoren vystup konverze:\nRETURN zvolí aktuální složku.\n> ")

if not output_path:
    output_path = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(input_path):
    raise FileNotFoundError(f"Cesta '{path}' neexistuje.")



invert_colors(input_path, output_path)

print('Haze bude spoko jak nikdy')

input('Zmackni Enter.')