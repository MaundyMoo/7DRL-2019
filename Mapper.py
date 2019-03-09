import Constants, BSP, Tiles, Image
class Map:
    def __init__(self, tileSheet: str):
        map = BSP.generate(30, 30)
        for row in map:
            print(row)
        self.spritesheet = Image.SpriteSheet(tileSheet, 32)
        self.map = self.__getTileMap(map)

    def __getTileMap(self, map):
        tiles = []
        #Could probably do this using map or filter or replace, one of those functions
        for y in range(len(map)):
            row = []
            for x in range(len(map[0])):
                if map[y][x]:
                    row.append(Tiles.Tile(gridPos=(x, y),
                                          collision=False,
                                          sprite=self.spritesheet.returnSprite(0, 0)))
                else:
                    row.append(Tiles.Tile(gridPos=(x, y),
                                           collision=True,
                                           sprite=self.spritesheet.returnSprite(1, 0)))
            tiles.append(row)
        return tiles

    def getMap(self):
        return self.map