from util import hex_to_int, int_to_hex

class Palette:
    def __init__(self):
        self.hex_list = []
        self.colors = []
        self.color_count = 16

        for i in range(self.color_count):
            self.hex_list.append("000000") 
        
        self.bake_color_list()

    def hex_to_color(self, hex):
        r_hex = hex[0] + hex[1]
        g_hex = hex[2] + hex[3]
        b_hex = hex[4] + hex[5]

        return [hex_to_int(r_hex), hex_to_int(g_hex), hex_to_int(b_hex), 255]

    def bake_color_list(self):
        self.colors = []

        for h in self.hex_list:
            self.colors.append(self.hex_to_color(h))
    

    def generate_pallete(self):
        self.hex_list = []

        for i in range(self.color_count):
            self.hex_list.append(input(f'Color #{i}:'))

        for i in range(self.color_count):
            print(self.hex_list[i])
        
        self.bake_color_list()
        self.save_hex(input("Save palette name: "))
    
    def generate_from_color(self, max_color):
        step = [max_color[0] / (self.color_count - 1),
                max_color[1] / (self.color_count - 1),
                max_color[2] / (self.color_count - 1)]

        self.hex_list.clear()
        for i in range(self.color_count):
            r = round(step[0] * i)
            g = round(step[1] * i)
            b = round(step[2] * i)
            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))
            self.hex_list.append(f"{r:02x}{g:02x}{b:02x}")
        self.bake_color_list()
        self.save_hex(input("Save palette name: "))

    def load_palette(self, str):
        self.hex_list = self.read_hex(str)
        self.bake_color_list()


    def read_hex(self, name):
        with open(f'palettes/{name}.plt', "r") as f:
            data = f.read().strip()

        hex_list = [data[i:i+6] for i in range(0, len(data), 6)]

        return hex_list

    def save_hex(self, name):
        with open(f'palettes/{name}.plt', "w") as f:
            save_str = ""

            for str in self.hex_list:
                save_str += str
            
            f.write(save_str)