class InforTable:
    count = 0

    def __init__(self, idTable, numberP, state, numberE):
        self.idTable = idTable
        self.numberP = numberP
        self.state = state
        self.numberE = numberE

        InforTable.count += 1

    def set_id(self, idTable):
        self.idTable = idTable

    def get_id(self):
        return self.idTable

    def set_NP(self, numberP):
        self.numberP = numberP

    def get_NP(self):
        return self.numberP

    def __bool__(self):
        if self.state == 0:
            return False
        elif self.state == 1:
            return True

    def set_NumberE(self, numberE):
        self.numberE = numberE

    def get_numberE(self):
        return self.numberE

    def show_Table(self):
        # print("\n+--------------------+")
        print(f"|ID                             :          {self.idTable}   |")
        print(f"|Số người tối đa trong một bàn  :          {self.numberP}   |")
        print(f"|Tình trạng bàn                 :         {bool(self.state)} |")
        print(f"|số người đang ngồi trên bàn này:          {self.numberE}   |")
        print("+----------------------------------------------+")


a = InforTable("2", "3", 1, "4")
b = InforTable("3", "4", 0, "6")
print(a.show_Table())
print(b.show_Table())
