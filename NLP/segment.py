import jieba
import jieba.analyse
import jieba.posseg as pseg

words = pseg.cut("化学学院位于哪个校区")
for word, flag in words:
    print('%s %s' % (word, flag))


seg_list = jieba.cut("化学学院位于哪个校区", HMM=False)  # 默认是精确模式
print(", ".join(seg_list))
