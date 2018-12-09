"""
    数値のデータ型
    https://docs.python.jp/3/tutorial/introduction.html
    int と float に加え、 Python は Decimal や Fraction などの他の数値型もサポートしています

"""


bin_num = 0b10
oct_num = 0o10
hex_num = 0x10

print('2進数表記で0b10 = ', bin_num)
print('8進数表記で0o10＝', oct_num)
print('16進数表記で0x10＝', hex_num)
# 2
# 8
# 16


print('足し算2+2=', 2 + 2)
print('引き算5−2=', 5 - 2)
print('かけ算10*3=', 10 * 3)
print('割り算10 / 3=', 10 / 3)

print("文字型と数値の連結には、数値を文字型に寄せる")
print("8/5 =" + str(8/5))

print("あるいは、こんな風にカンマで区切って渡す方がprintの場合は良い")
print("8/5ここ =" , 8/5)

print("割り算は浮動小数点を返す")
print("17/3 = " + str(17/3))
print("3/5 = " , 3/5)


print("// による割り算では、整数で結果を返す ？？切り捨てだ")
print("17//3 = " + str(17//3))
print("16//3 = " + str(16//3))



print("%であまりを返す")
print("17%3 = " + str(17%3))

print("べき乗　いわゆる　同じ数値の掛け算")
print("5の２乗は 5**2　＝" + str(5**2))


print("4 * 3.75 - 1 =" + str(4*3.75-1))

print('虚数はjで表す')
kyosuu = 3 + 4j
print(kyosuu)
print(type(kyosuu))

print("大きい数字の時に、任意箇所に_を入れることができるようになった100_000_000 ＝ ", 100_000_000)

