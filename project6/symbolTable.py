class Table:
    def __init__(self):
        self.Dict = {'R0': 0,'R1': 1,'R2': 2,'R3': 3, 'R4': 4, 'R5': 5,
                        'R6': 6,'R7': 7,'R8': 8,'R9': 9,'R10': 10,'R11': 11,
                        'R12': 12,'R13': 13,'R14': 14,'R15': 15,'SCREEN': 16384,
                        'KBD': 24576,'SP': 0,'LCL': 1,'ARG': 2,'THIS': 3,'THAT': 4
                    }

    # def printTable(self):
    #     # self.Dict['Bleh'] = 20
    #     for k, v in self.Dict.items():
    #         print(str(k) + ":" + str(v))

    def get(self, key):
        if key in self.Dict:
            # print(key + " Exists !")
            return self.Dict.get(key)

    def add(self, key, value):
        if key not in self.Dict:
            # print(key + " added !")
            # print(value)
            self.Dict[key] = value

    def isInTable(self, key):
        if key in self.Dict:
            return True
        else:
            return False