# %s 标是：将内容转换成字符串，放入占位符
# %d: 将内容转换成为整数，放入占位位置
# %f: 将内容转换成浮点型，放入占位位置

name = "张三"
set_up_year = 2005
stock_price = 19.998
message = "我是%s, 我的公司成立于%d, 公司股价是%f" % (name, set_up_year, stock_price)
print(message)

# 占位精度控制
# m: 控制宽度，要求是数字(很少使用)
# .n: 控制小数点精度，会进行小数的四舍五入
# 例如：%5d: 将整数的宽度控制在5位，如数字11，被设置位5d,就会变成【】【】【】11， 用三个空格补足宽度
# 例如：%5.2f: 标是将宽度控制为5，小数点精度控制位2

num1 = 11
num2 = 22.234
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字22.234宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字22.234四舍五入是：%.2f" % num2)

# 快速格式化字符串前面加f: f"内容{变量}"的格式来快速格式化
print(f"我是{name}, 我的公司成立于{set_up_year}, 我今天的股价是{stock_price}")
print(f"我是{name}, 我的公司成立于{set_up_year:5}, 我今天的股价是{stock_price:.2f}")

# 对表达式格式化
print("1*1的表达式结果是：%d" % (1*1))
print(f"1*1的表达式结果是：{1*1}")
print("字符串在Python中的类型是：%s" % type('字符串'))

'''
练习：格式化输出小程序
需求：
company_name
stock_price
stock_code
stock_price_daily_growth_factor
growth_days
经过growth_days, 股价达到了多少
'''
company_name = '顺通'
stock_price = 29.2354
stock_code = 'A234'
stock_price_daily_growth_factor = 1.2  # 增长系数
growth_days = 7

final_stock_price = stock_price*stock_price_daily_growth_factor**growth_days
print(f"公司名：{company_name},股票代码：{stock_code}, 当前股价：{stock_price}, 每日增长系数：{stock_price_daily_growth_factor},经过了{growth_days}的增长之后,股票价格达到了{final_stock_price:.2f}")



