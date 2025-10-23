import util, pygame

class Texture:
    def __init__(self, size, pal = util.Palette, pxl_size = 16):
        self.palette = pal
        self.map : list = []
        self.size = size
        self.surf = pygame.Surface(size)

        self.dirty = False
        self.str = ''
        self.map_str = ''
        self.pixel_size = pxl_size

    def load_sprite_map(self, sprite_name, pal = None):
        self.str = ""

        with open(f'sprites/{sprite_name}.spt', "r") as f:
            data = f.read().strip()
            self.str = data
        
        dim_1_str = ''
        dim_2_str = ''

        dim_1_str += self.str[0]
        dim_1_str += self.str[1]
        dim_2_str += self.str[2]
        dim_2_str += self.str[3]

        self.size = [util.hex_to_int(dim_1_str), util.hex_to_int(dim_2_str)]

        self.map_str = ''

        for i, char in enumerate(self.str):
            if i >= 4:
                self.map_str += self.str[i]
        
        for i, char in enumerate(self.map_str):
            width = self.size[0]
            current_y = i // width
            current_x = i % width
            self.map.append([current_x, current_y, char])

        self.dirty = True

        if len(self.map_str) < 255:
            print("Size difference error")

    def bake_map(self):
        self.surf = pygame.Surface([self.size[0] * self.pixel_size, self.size[1] * self.pixel_size]).convert_alpha()
        self.surf.fill([0,0,0,0])
        
        for l in self.map:
            coords = [l[0], l[1]]
            char = l[2]

            if char == 'f':
                continue

            col = self.palette.colors[util.hex_to_int(char)]
            pygame.draw.rect(self.surf, col, [coords[0] * self.pixel_size, coords[1] * self.pixel_size, self.pixel_size, self.pixel_size])
        
        self.dirty = False
        print(len(self.map), self.size)
    
    def draw(self, surf, position):
        if self.dirty: self.bake_map()
        surf.blit(self.surf, position)