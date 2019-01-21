import random
import time


def get_order_sn():
    #获取订单号，保证唯一
    s = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    order_sn = ''
    for i in range(20):

        order_sn += random.choice(s)

    order_sn += str(time.time())

    return order_sn


