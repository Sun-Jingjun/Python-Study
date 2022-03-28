try:
    a = 10 / 0
except Exception as e:
    print('非法error:{}'.format(e))
finally:
    print('一定会执行')

