
class Grid:

    def __init__(self, dimension, visual):
        self.symbol_representation = visual
        self.columns = dimension
        self.rows = dimension
        if dimension % 2 == 0:
            self.centre = [(dimension//2), (dimension//2)-1]
            self.matrix = [[0] * self.columns for n in range(self.rows+1)]
        else:
            self.centre = [(dimension//2), (dimension//2)]
            self.matrix = [[0] * self.columns for n in range(self.rows)]
        self.generate_spiral()
    
    def is_prime(self, n):
        if n in [1, 2]:
            return False
        for i in range(2, (n-1)):
            if n % i == 0:
                return False
        return True

    def init_primes(self):
        current_pos = self.centre
        direction = "E"
        step = 1
        counter = 0
        digit = 1
        while digit <= (self.rows*self.rows):
            if self.is_prime(digit):
                self.matrix[current_pos[0]][current_pos[1]] = "    "
            else:
                self.matrix[current_pos[0]][current_pos[1]] = digit
            if counter != step:
                if direction == "E":
                    current_pos[1] += 1
                    counter += 1
                    digit +=1
                elif direction == "N":
                    current_pos[0] -= 1
                    counter += 1
                    digit += 1
                elif direction == "W":
                    current_pos[1] -= 1
                    counter += 1
                    digit+=1
                elif direction == "S":
                    current_pos[0] += 1
                    counter += 1
                    digit+=1
            elif counter == step:
                if direction == "E":
                    direction = "N"
                    counter = 1
                    digit += 1
                    current_pos[0] -= 1
                elif direction == "N":
                    direction = "W"
                    step += 1
                    counter = 1
                    digit += 1
                    current_pos[1] -= 1
                elif direction == "W":
                    direction = "S"
                    counter = 1
                    digit += 1
                    current_pos[0] += 1
                elif direction == "S":
                    direction = "E"
                    step += 1
                    counter = 1
                    digit += 1
                    current_pos[1] += 1

    def generate_spiral(self):
        current_pos = self.centre
        direction = "E"
        step = 1
        counter = 0
        digit = 1
        while digit <= (self.rows*self.rows):
            self.matrix[current_pos[0]][current_pos[1]] = digit
            if counter != step:
                if direction == "E":
                    current_pos[1] += 1
                    counter += 1
                    digit +=1
                elif direction == "N":
                    current_pos[0] -= 1
                    counter += 1
                    digit += 1
                elif direction == "W":
                    current_pos[1] -= 1
                    counter += 1
                    digit+=1
                elif direction == "S":
                    current_pos[0] += 1
                    counter += 1
                    digit+=1
            elif counter == step:
                if direction == "E":
                    direction = "N"
                    counter = 1
                    digit += 1
                    current_pos[0] -= 1
                elif direction == "N":
                    direction = "W"
                    step += 1
                    counter = 1
                    digit += 1
                    current_pos[1] -= 1
                elif direction == "W":
                    direction = "S"
                    counter = 1
                    digit += 1
                    current_pos[0] += 1
                elif direction == "S":
                    direction = "E"
                    step += 1
                    counter = 1
                    digit += 1
                    current_pos[1] += 1

                
            
    
    def __str__(self):
        return_str = ""
        if self.symbol_representation == True:
            for i in range(self.rows):
                for x in range(self.columns):
                    if self.is_prime(self.matrix[i][x]):
                        return_str += "|"
                    else:
                        return_str += "-"
                return_str += "\n"
        else:
            for i in range(self.rows):
                for x in range(self.columns):
                    if (self.matrix[i][x] == "##"):
                        return_str += str(self.matrix[i][x]) + " "
                    elif (self.matrix[i][x] < 10):
                        return_str += str(self.matrix[i][x]) + "    "
                    elif (self.matrix[i][x] >= 10 and self.matrix[i][x] < 100):
                        return_str += str(self.matrix[i][x]) + "   "
                    elif (self.matrix[i][x] >= 100 and self.matrix[i][x] < 1000):
                        return_str += str(self.matrix[i][x]) + "  "
                    else:
                        return_str += str(self.matrix[i][x]) + " "
                return_str += "\n"
        return return_str


spiral = Grid(100, True)
print(spiral)