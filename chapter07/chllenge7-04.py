answers = [3, 7, 10]

while True:
    a = input("数字を入力してください（qで終了）: ")

    if a == "q":
        print("終了します")
        break

    elif a.isdigit():
        if int(a) in answers:
            print("正解")
        else:
            print("不正解")

    else:
        print("数字を入力するか q で終了します")
