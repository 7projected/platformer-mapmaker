def hex_to_int(hex):
    return int(hex, 16)

def int_to_hex(i):
    return hex(i)

class Palette:
    def __init__(self):
        self.hex_list = []
        self.color_list = []
        self.colors = 8

        for i in range(self.colors):
            self.hex_list.append("000000") 
        
        self.bake_color_list()

    def hex_to_color(self, hex):
        r_hex = hex[0] + hex[1]
        g_hex = hex[2] + hex[3]
        b_hex = hex[4] + hex[5]

        return [hex_to_int(r_hex), hex_to_int(g_hex), hex_to_int(b_hex)]

    def bake_color_list(self):
        self.color_list = []

        for h in self.hex_list:
            self.color_list.append(self.hex_to_color(h))
    

    def generate_pallete(self):
        self.hex_list = []

        for i in range(self.colors):
            self.hex_list.append(input(f'Color #{i}:'))

        for i in range(self.colors):
            print(self.hex_list[i])
        
        self.bake_color_list()
        self.save_hex(input("Save palette name: "))

    def load_palette(self):
        self.hex_list = self.read_hex(input("Load palette name: "))
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