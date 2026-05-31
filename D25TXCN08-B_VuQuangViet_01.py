import json

try:
    with open("data.json", "r", encoding="utf-8") as file:
        player_list = json.load(file)
except:
    player_list = []

while True:

    choice=input('''
\n========= QUẢN LÝ CẦU THỦ =========
1. Hiển thị danh sách cầu thủ
2. Thêm mới cầu thủ
3. Cập nhật thông tin cầu thủ
4. Xóa cầu thủ
5. Tìm kiếm cầu thủ
6. Sắp xếp danh sách cầu thủ
7. Thống kê cầu thủ theo danh hiệu
8. Thống kê số lượng cầu thủ
9. Hiển thị cầu thủ có điểm cao nhất và thấp nhất
0. Thoát
Nhập lựa chọn: ''').strip()

    match choice:
        case "1":
            if len(player_list) == 0:
                print("Danh sách cầu thủ trống")
                continue

            print(f"{'Mã CT':<10} | {'Tên cầu thủ':<25} | {'Số trận':<8} | {'Bàn thắng':<10} | {'Kiến tạo':<10} | {'Điểm':<8} | {'Danh hiệu'}")
            print("-" * 100)

            for player in player_list:
                print(
                    f"{player['ma_ct']:<10} | "
                    f"{player['ten_ct']:<25} | "
                    f"{player['so_tran']:<8} | "
                    f"{player['ban_thang']:<10} | "
                    f"{player['kien_tao']:<10} | "
                    f"{player['diem_thanh_tich']:<8} | "
                    f"{player['danh_hieu']}"
                )

        case "2":
            while True:
                player_id = input("Nhập mã cầu thủ: ").upper().strip()

                if player_id == "":
                    print("Không được để trống")
                    continue

                if any(player["ma_ct"] == player_id for player in player_list):
                    print("Mã cầu thủ đã tồn tại")
                    continue
                break

            while True:
                name = input("Nhập tên cầu thủ: ").strip()

                if name == "":
                    print("Tên không được để trống")
                    continue
                break

            while True:
                match_numbers = input("Nhập số trận: ")
                
                if not match_numbers.lstrip("-").isdigit():
                    print("Vui lòng nhập số")
                    continue

                match_numbers = int(match_numbers)
                if match_numbers < 0:
                    print("Phải >= 0")
                    continue
                break

            while True:
                goals = input("Nhập số bàn thắng: ")
                
                if not goals.lstrip("-").isdigit():
                    print("Vui lòng nhập số")
                    continue
                
                goals = int(goals)
                if goals < 0:
                    print("Phải >= 0")
                    continue
                break

            while True:
                goal_creating = input("Nhập số bàn kiến tạo: ")
                
                if not goal_creating.lstrip("-").isdigit():
                    print("Vui lòng nhập số")
                    continue
                
                goal_creating = int(goal_creating)
                if goal_creating < 0:
                    print("Phải >= 0")
                    continue
                break

            score = goals * 2 + goal_creating

            if score > 40:
                title = "Vàng"
            elif score> 20:
                title = "Bạc"
            else:
                title = "Đồng"

            player = {
                "ma_ct": player_id,
                "ten_ct": name,
                "so_tran": match_numbers,
                "ban_thang": goals,
                "kien_tao": goal_creating,
                "diem_thanh_tich": score,
                "danh_hieu": title
            }

            player_list.append(player)

            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(player_list, file, ensure_ascii=False, indent=4)

            print("Thêm cầu thủ thành công")

        case "3":
            while True:
                update_id = input("Nhập mã cầu thủ cần cập nhật: ").upper().strip()

                if update_id == "":
                    print("Không được để trống")
                    continue
                break

            for player in player_list:
                if player["ma_ct"] == update_id:
                    while True:
                        new_goals = input("Nhập số bàn thắng mới: ")
                        
                        if not new_goals.lstrip("-").isdigit():
                            print("Vui lòng nhập số")
                            continue
                        
                        new_goals = int(new_goals)
                        if new_goals < 0:
                            print("Phải >= 0")
                            continue
                        break

                    while True:
                        new_creating = input("Nhập số bàn kiến tạo mới: ")
                        
                        if not new_creating.lstrip("-").isdigit():
                            print("Vui lòng nhập số")
                            continue
                        
                        new_creating = int(new_creating)
                        if new_creating < 0:
                            print("Phải >= 0")
                            continue
                        break

                    player["ban_thang"] = new_goals
                    player["kien_tao"] = new_creating

                    player["diem_thanh_tich"] = (player["ban_thang"] * 2 + player["kien_tao"])

                    if player["diem_thanh_tich"] > 40:
                        player["danh_hieu"] = "Vàng"
                    elif player["diem_thanh_tich"] > 20:
                        player["danh_hieu"] = "Bạc"
                    else:
                        player["danh_hieu"] = "Đồng"

                    with open("data.json", "w", encoding="utf-8") as file:
                        json.dump(player_list, file, ensure_ascii=False, indent=4)

                    print("Cập nhật thành công")
                    break

            else:
                print("Không tìm thấy cầu thủ")

        case "4":
            while True:
                delete_id = input("Nhập mã cầu thủ cần xóa: ").upper().strip()

                if delete_id == "":
                    print("Không được để trống")
                    continue
                break

            for player in player_list:
                if player["ma_ct"] == delete_id:
                    confirm = input("Bạn có chắc muốn xóa? (Y/N): ").upper()
                    if confirm == "Y":
                        player_list.remove(player)
                        with open("data.json", "w", encoding="utf-8") as file:
                            json.dump(player_list, file, ensure_ascii=False, indent=4)

                        print("Xóa thành công")
                        break
                    elif confirm == "N":
                        print("Đã hủy thao tác xóa cầu thủ")
                    else:
                        print("Lựa chọn không hợp lê, vui lòng nhập 'N' hoặc 'Y'")

                    break

            else:
                print("Không tìm thấy cầu thủ")

        case "5":
            keyword = input("Nhập mã hoặc tên cầu thủ: ").strip()

            found = False

            for player in player_list:
                if keyword.upper() in player["ma_ct"] or keyword.lower() in player["ten_ct"].lower():

                    if not found:
                        print(f"{'Mã CT':<10} | {'Tên cầu thủ':<25} | {'Điểm':<8} | {'Danh hiệu'}")
                        print("-" * 70)

                    print(
                        f"{player['ma_ct']:<10} | "
                        f"{player['ten_ct']:<25} | "
                        f"{player['diem_thanh_tich']:<8} | "
                        f"{player['danh_hieu']}"
                    )

                    found = True

            if not found:
                print("Không tìm thấy cầu thủ")

        case "6":
            sub_choice = input('''
1. Sắp xếp theo điểm thành tích giảm dần
2. Sắp xếp theo bàn thắng giảm dần
Nhập lựa chọn: ''').strip()

            match sub_choice:
                case "1":
                    player_list.sort(key=lambda x: x["diem_thanh_tich"], reverse=True)
                    with open("data.json", "w", encoding="utf-8") as file:
                        json.dump(player_list, file, ensure_ascii=False, indent=4)
                    print("Đã sắp xếp theo điểm")

                case "2":
                    player_list.sort(key=lambda x: x["ban_thang"], reverse=True)
                    with open("data.json", "w", encoding="utf-8") as file:
                        json.dump(player_list, file, ensure_ascii=False, indent=4)
                    print("Đã sắp xếp theo bàn thắng")

                case _:
                    print("Lựa chọn ko hợp lệ, vui lòng nhập 1 hoặc 2")

        case "7":
            gold = 0
            silver = 0
            bronze = 0

            for player in player_list:
                if player["danh_hieu"] == "Vàng":
                    gold += 1
                elif player["danh_hieu"] == "Bạc":
                    silver += 1
                else:
                    bronze += 1

            print(f"Vàng: {gold}")
            print(f"Bạc: {silver}")
            print(f"Đồng: {bronze}")

        case "8":
            gold = 0
            silver = 0
            bronze = 0

            for player in player_list:
                if player["danh_hieu"] == "Vàng":
                    gold += 1
                elif player["danh_hieu"] == "Bạc":
                    silver += 1
                else:
                    bronze += 1

            print("\n===== THỐNG KÊ SỐ LƯỢNG CẦU THỦ THEO DANH HIỆU =====")
            print(f"Danh hiệu Vàng có {gold} cầu thủ")
            print(f"Danh hiệu Bạc có {silver} cầu thủ")
            print(f"Danh hiệu Đồng có {bronze} cầu thủ")

        case "9":
            if len(player_list) == 0:
                print("Danh sách trống")
                continue

            best_player = player_list[0]
            weak_player = player_list[0]

            for player in player_list:
                if player["diem_thanh_tich"] > best_player["diem_thanh_tich"]:
                    best_player = player

                if player["diem_thanh_tich"] < weak_player["diem_thanh_tich"]:
                    weak_player = player

            print("\n=== CẦU THỦ CÓ ĐIỂM THÀNH TÍCH CAO NHẤT ===")
            for player in player_list:
                if player["diem_thanh_tich"] == best_player["diem_thanh_tich"]:
                    print(player)

            print("\n=== CẦU THỦ CÓ ĐIỂM THÀNH TÍCH THẤP NHẤT ===")
            for player in player_list:
                if player["diem_thanh_tich"] == weak_player["diem_thanh_tich"]:
                    print(player)

        case "10":
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại lựa chọn 1-10")
