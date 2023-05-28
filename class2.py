from class1 import InforTable

listTable = []
while True:
    print(f'''
    0. Thoát trương trình
    1. Thêm bàn
    2. Sửa số người có thể ngồi trong 1 bàn
    3. Xóa bàn
    4. Xem thông tin tất cả các bàn
    5. Xem thông tin theo ID bàn
    6. cập nhật thông tin bàn
    7. Số lượng bàn sẵn có
    ''')
    select = input("Lựa chọn chức năng: ")
    if str(select).isdigit():
        select = int(select)
        if select == 0:
            break
        elif select == 1:
            slTable = int(input("Nhập số lượng bàn: "))
            demTb = 1
            while demTb <= slTable:
                print("NOTE: tình trạng bàn nhập 0 hoặc 1")
                print(f"Đây là bàn số {demTb}")
                id1 = input("Id của bàn: ")
                number = input("Số người tối đa có thể ngồi trong bàn là: ")
                st = int(input("nhập tình trạng bàn: "))
                slE = input("Nhập số lượng người đang ngồi trên bàn: ")
                tb = InforTable(id1, number, st, slE)
                listTable.append(tb)
                demTb += 1
        elif select == 2:
            id2 = input("Nhập ID bàn cần sửa thông tin: ")
            for i in listTable:
                if i.get_id() == id2:
                    i.set_NP(input("Nhập số lượng mới: "))
                    i.show_Table()
        elif select == 3:
            id3 = input("Nhạp ID bàn cần xóa: ")
            for i in listTable:
                if i.get_id() == id3:
                    listTable.remove(i)
                    print(f"Đã xóa {id3} thành công!")
        elif select == 4:
            if len(listTable) == 0:
                print("Hiện tại không còn bàn nào trống !!!")
            else:
                print("+----------------------------------------------+")
                for i in listTable:
                    i.show_Table()

    else:
        print("WARNING!!!")
        print("ban phai nhap so")
