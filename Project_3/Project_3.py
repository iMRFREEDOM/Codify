import random

# 1. Area 
class GameMap:
    def __init__(self):
        self.area = [["*" for _ in range(10)] for _ in range(10)]

    def get_random_position(self):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.area[x][y] == "*":
                return x, y

# 2. Player
class Player:
    def __init__(self, x, y):
        self.health = 100
        self.x = x
        self.y = y
        self.has_sword = False

# 3. Enemy
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Game:
    def __init__(self):
        self.map_obj = GameMap()
        
        # O'yinchini tasodifiy joylashtirish
        px, py = self.map_obj.get_random_position()
        self.player = Player(px, py)
        self.map_obj.area[px][py] = "P"  # P - Player
        
        # Placing sword
        sx, sy = self.map_obj.get_random_position()
        self.map_obj.area[sx][sy] = "S"  # S - Sword
        
        # Placing medkit
        mx, my = self.map_obj.get_random_position()
        self.map_obj.area[mx][my] = "M"  # M - Medkit
        
        # Placing treasure
        tx, ty = self.map_obj.get_random_position()
        self.map_obj.area[tx][ty] = "T"  # T - Treasure
        
        # placing enemies
        self.enemies = []
        num_enemies = int(input("How many enemies you want (1-5): "))
        for _ in range(num_enemies):
            ex, ey = self.map_obj.get_random_position()
            self.map_obj.area[ex][ey] = "E"  # E - Enemy
            self.enemies.append(Enemy(ex, ey))

    def draw_map(self):
        print("\n  ----- Area -----")
        for row in self.map_obj.area:
            print(" ".join(row))
        print(f"❤️ Health (HP): {self.player.health} | ⚔️ Sword: {'Ha' if self.player.has_sword else 'No'}")

    def battle_logic(self):
        if self.player.has_sword:
            print("\n You killed the monster and your sword has broken")
            self.player.has_sword = False
        else:
            self.player.health -= 50
            if self.player.health <= 0:
                print("\n💀 You're dead.")
            else:
                print(f"\n Enemy attacked you! Remaining HP: {self.player.health}")

    def move_player(self, direction):
        old_x, old_y = self.player.x, self.player.y
        new_x, new_y = old_x, old_y

        if direction == "w": new_x -= 1
        elif direction == "s": new_x += 1
        elif direction == "a": new_y -= 1
        elif direction == "d": new_y += 1
        else: return

        target = self.map_obj.area[new_x][new_y]

        if target == "E":
            self.battle_logic()
            if self.player.health <= 0: return

        elif target == "S":
            print("\n You found a sword!")
            self.player.has_sword = True

        elif target == "M":
            print("\n You found a medkit! HP restored.")
            self.player.health = 100

        elif target == "T":
            print("\n🏆 Victory! You found the treasure!")
            self.player.health = 0  # O'yinni tugatish uchun
            return

        self.map_obj.area[old_x][old_y] = "*"
        self.player.x, self.player.y = new_x, new_y
        self.map_obj.area[new_x][new_y] = "P"

    def play(self):
        while self.player.health > 0:
            self.draw_map()
            move = input("Move (W, A, S, D): ").lower()
            self.move_player(move)

if __name__ == "__main__":
    game = Game()
    game.play()