"""
    コレクション、繰り返しを処理するforについて確認

"""



print("""\
words = ['猫','犬','牛','馬']
for word in words:
    print(word)
と書いた場合は
""")

words = ['猫','犬','牛','馬']
for word in words:
    print(word)


print("""
2ばんめとして　列挙内容を空にしました
words = []
for word in words:
    print(word)
""")

words = []
for word in words:
    print(word)

print("ここの上までがfor内のprintです")


print("*************************")

print("range確認")

start = 0
end = 10
increment = 2
for x in range(start, end, increment):
    print(x)


print("*************************")

print("continueの説明用途　１。先ずは素直に全部出力")

for x in range(5):
    print("x = ", x)


print("continueの説明用途　２。X＝３の時は何もしない（次のforへ")
for x in range(5):
    if x == 3:
        continue
    print("x = ", x)

print("breakの説明用途　xが3になったら、for全体を抜ける")
for x in range(5):
    if x == 3:
        break
    print("x = ", x)


print("""
elseについて。 forの中で、breakを使用しなかった場合に、else説を実行する、と言う仕組みとのこと
次の処理ではwordsが空配列なのでelseに行きます
""")

words = []
for word in words:
    print(word)
    break
else:
    print('これは意図通りに見える処理 elseに処理をかける')


print("""
要注意の箇所だったので記載

words = ['ウミウシ','おたまじゃくし','殿様蛙']
for word in range(5):
    if word == 'シーラカンス':
        break
else:
    print('forループの中に入ったが、breakが実行されなかったのでelseが実行')

""")

words = ['ウミウシ','おたまじゃくし','殿様蛙']
for word in range(5):
    if word == 'シーラカンス':
        break
else:
    print('forループの中に入ったが、breakが実行されなかったのでelseが実行')


for x in range(3):
    print(x)
    if (x < 2) :
        print("x=", x)
        continue
    print("x の値でbreakします", x)
    break
else:
    print('else通りました')
    print(x)


print('https://docs.python.jp/3/tutorial/datastructures.html#tut-loopidioms ループのテクニック')

print("オブジェクト要素のプロパティ名と値を出せている")
man= {'namae': 'hoge', '職業': '勇者'}
for k, v in man.items():
    print(k,v)



print('enumerateを使用することで、indexの何番目かも出せる')
for i, v in enumerate(['hoge','fuga','piyo']):
    print(i, v)


print('2つのコレクションを同時にループできる')
questions=['a','b','c','d']
answers  =['A','B','C','D']
for q, a in zip(questions, answers):
    print(q, a)



