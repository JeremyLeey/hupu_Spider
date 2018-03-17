import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
with open("H://hupubxj_2018-3-13.txt", "r") as fp:
    text_from_file = fp.read()

wordlist_after_jieba = jieba.cut(text_from_file, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)

# 支持中文选项
font = r'C:\Windows\Fonts\simsun.ttc'
text = """大腿
真白
胸
真大
啧啧
"""
print(wl_space_split)
cloud = WordCloud(
    max_words=60,
    font_path=font,
    background_color="white",
    width=1000,
    height=860,
    margin=2)

my_wordcloud = cloud.generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

