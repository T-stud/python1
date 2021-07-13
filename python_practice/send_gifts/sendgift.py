have_gift = False


def send():
    global have_gift
    print("发礼物了")
    have_gift = True


def show():
    if have_gift == True:
        print('收到礼物')
    else:
        print('没有礼物')


print(f"变量值为{__name__}")
# if __name__ == '__main__':
#     send()
#     show()
