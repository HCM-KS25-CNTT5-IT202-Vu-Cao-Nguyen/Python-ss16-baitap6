def find_blood_bag_index(inventory, blood_id):
    """
    Tìm vị trí túi máu trong kho theo mã túi máu.

    Args:
        inventory (list): Danh sách túi máu.
        blood_id (str): Mã túi máu cần tìm.

    Returns:
        int: Vị trí túi máu nếu tìm thấy, ngược lại trả về -1.
    """
    blood_id = blood_id.strip().upper()

    for index, record in enumerate(inventory):
        if record.startswith(blood_id + "-"):
            return index

    return -1


def display_inventory(inventory):
    """
    Hiển thị danh sách túi máu và tổng thể tích máu.

    Args:
        inventory (list): Danh sách túi máu.

    Returns:
        None
    """
    if not inventory:
        print("Kho máu hiện chưa có túi máu nào.")
        return

    total_volume = 0

    print("\n--- DANH SÁCH KHO MÁU ---")
    print("Mã Túi | Người Hiến       | Nhóm Máu | Thể Tích | Ngày Hết Hạn")
    print("-" * 62)

    for record in inventory:
        parts = record.rsplit("-", 2)

        info = parts[0].split("-")
        blood_id = info[0]
        donor_name = info[1]
        blood_type = info[2]

        volume = parts[1]
        expiry = parts[2]

        total_volume += int(volume)

        print(
            f"{blood_id:<6} | "
            f"{donor_name:<16} | "
            f"{blood_type:<8} | "
            f"{volume} ml{' ' * (4 - len(volume))}| "
            f"{expiry}"
        )

    print("-" * 62)
    print(f"Tổng thể tích máu trong kho: {total_volume} ml.")


def add_blood_bag(inventory):
    """
    Thêm túi máu mới vào kho.

    Args:
        inventory (list): Danh sách túi máu.

    Returns:
        None
    """
    print("\n--- NHẬP TÚI MÁU MỚI ---")

    blood_id = input("Nhập mã túi máu mới: ").strip().upper()

    if not blood_id:
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    if find_blood_bag_index(inventory, blood_id) != -1:
        print(f"\nLỗi: Mã túi máu {blood_id} đã tồn tại! Vui lòng nhập mã khác.")
        return

    donor_name = input("Nhập tên người hiến: ").strip().title()

    if not donor_name:
        print("\nLỗi: Tên người hiến không được để trống!")
        return

    blood_type = input("Nhập nhóm máu: ").strip().upper()

    volume = input("Nhập thể tích (ml): ").strip()

    if not volume.isdigit() or int(volume) <= 0:
        print("\nLỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return

    expiry = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()

    blood_record = "-".join([
        blood_id,
        donor_name,
        blood_type,
        volume,
        expiry
    ])

    inventory.append(blood_record)

    print(f"\nThành công: Đã nhập túi máu {blood_id} vào kho!")
    print("\nSau khi chuẩn hóa, dữ liệu được lưu vào list là:")
    print(blood_record)


def update_expiry(inventory):
    """
    Cập nhật ngày hết hạn của túi máu.

    Args:
        inventory (list): Danh sách túi máu.

    Returns:
        None
    """
    print("\n--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")

    blood_id = input("Nhập mã túi máu cần cập nhật: ").strip().upper()

    if not blood_id:
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_bag_index(inventory, blood_id)

    if index == -1:
        print(f"\nLỗi: Không tìm thấy túi máu {blood_id} trong kho!")
        return

    new_expiry = input("Nhập ngày hết hạn mới: ").strip()

    record_parts = inventory[index].rsplit("-", 2)

    record_parts[2] = new_expiry

    inventory[index] = "-".join(record_parts)

    print(f"\nThành công: Đã cập nhật ngày hết hạn cho túi máu {blood_id}!")


def remove_blood_bag(inventory):
    """
    Xuất hoặc hủy túi máu khỏi kho.

    Args:
        inventory (list): Danh sách túi máu.

    Returns:
        None
    """
    print("\n--- XUẤT / HỦY TÚI MÁU ---")

    blood_id = input("Nhập mã túi máu cần xuất/hủy: ").strip().upper()

    if not blood_id:
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_bag_index(inventory, blood_id)

    if index == -1:
        print(f"\nLỗi: Không tìm thấy túi máu {blood_id} trong kho!")
        return

    inventory.pop(index)

    print(f"\nThành công: Đã xuất túi máu {blood_id} khỏi kho!")


def main():
    """
    Hàm điều khiển menu chính của chương trình.

    Returns:
        None
    """
    blood_inventory = [
        "BL001-Nguyen Van A-O+-250-31/12/2026",
        "BL002-Tran Thi B-A--350-15/11/2026",
        "BL003-Le Van C-AB+-250-20/10/2026"
    ]

    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
        print("1. Xem danh sách túi máu trong kho")
        print("2. Nhập túi máu mới")
        print("3. Gia hạn / Sửa ngày hết hạn")
        print("4. Xuất / Hủy túi máu")
        print("5. Thoát chương trình")
        print("========================================")

        choice = input("Chọn chức năng (1-5): ").strip()

        match choice:
            case "1":
                display_inventory(blood_inventory)

            case "2":
                add_blood_bag(blood_inventory)

            case "3":
                update_expiry(blood_inventory)

            case "4":
                remove_blood_bag(blood_inventory)

            case "5":
                print("Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!")
                break

            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")


if __name__ == "__main__":
    main()