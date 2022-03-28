score_str = input('请输入你的成绩：')

score = int(score_str)

if score < 0 or score > 100:
    print('成绩不在范围内，非法')
elif score > 80:
    print('good')
elif score > 60:
    print('及格')
else:
    print('不及格')
