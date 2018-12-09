"""
    文字リテラルの確認
    macにおける \ の入力の仕方は、option + ¥ 

"""



aaa="二重引用符で入れたばあい"
print(aaa)



bbb='一重引用符で入れた場合'

print(bbb)

ccc="二重引用符の途中に ' を入れる    "
print(ccc)


print('C:\some\nameは、　\の後にnを入れると改行文字になる')  
print(r'C:\some\name頭にrawを入れる')  
print(r"print(r'C:\some\name頭にrawを入れる')  ")


ddd='二重引用符の途中に\' を入れる'
print(ddd)


print("""
このように複数行の
入力をすることも
可能
""")

print("""\
こちらは行末の\
改行を含む、含まない設定によって、ソースコード上の見た目と\
実際に出力される内容を
別にしています
""")


print("あいう*3 =" + "あいう" * 3)

print("py" 'thon')



some_list =['aa','bb','cc']
ttt = f'list:item:{some_list[0]}'
print('String.format的なやり方が可能です', ttt)