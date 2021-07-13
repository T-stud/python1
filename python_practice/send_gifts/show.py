# from gifts import have_gift
import gifts


def show():
    if gifts.have_gift == True:
        print('收到礼物')
    else:
        print('没有礼物')
