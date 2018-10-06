## 地址分词自然语言处理项目


### 依赖

* Python3
* github.com/fxsjy/jieba

### 项目结构

```
|
|- README.md		说明文件
|
|- analyse_weight.py	Jieba词频和权重分析
|- split_core.py        Jieba分词
|- test_dicts           Jieba测试自定义词典
|
|- parse_address        新地址分词核心
|- address_dict         新地址分词所需的数据和字典资料
|
|- sample.txt           输入样例文件
|- test.txt             小规模,高覆盖百分比,测试样例

|
```

### 用法

核心入口为``parse_address.py``,用法详见具体``.py``文件。

### 效果

```
[原文]
东城区东内北小街24号楼-10-202

[区]东城
[街道]东内北小街
[小区]
[楼号]24号楼
[单元]10
[门牌]10-202
 

[附加信息]
[~街道和小区]东内北小街
[~单元和门牌]10-202

[working_line]-10-202



[原文]
西城府右街中南海紫光阁101

[区]西城
[街道]府右街
[小区]东内北小街
[楼号]24号楼
[单元]10
[门牌]10-202
 

[附加信息]
[~街道和小区]东内北小街
[~单元和门牌]10-202

[working_line]中南海紫光阁101



[原文]
北京市海淀区羊坊店街道中雅大厦甲8号楼603

[区]海淀
[街道]羊坊店街道
[小区]中雅大厦甲
[楼号]8号楼
[单元]10
[门牌]603
 

[附加信息]
[~街道和小区]羊坊店街道中雅大厦甲
[~单元和门牌]603

[working_line]中雅大厦甲603



[原文]
东城区东扬威街309-3-701

[区]东城
[街道]东扬威街
[小区]羊坊店街道中雅大厦甲
[楼号]8号楼
[单元]10
[门牌]603
 

[附加信息]
[~街道和小区]羊坊店街道中雅大厦甲
[~单元和门牌]603

[working_line]309-3-701



[原文]
崇文区东内北小街24号楼11-402

[区]东城
[街道]东内北小街
[小区]
[楼号]24号楼
[单元]11
[门牌]11-402
 

[附加信息]
[~街道和小区]东内北小街
[~单元和门牌]11-402

[working_line]11-402



[原文]
昌平区龙域北街万科金域国际B座1603
[区]昌平
[街道]龙域北街
[小区]万科金域国际
[楼号]B座
[单元]11
[门牌]1603 

[附加信息]
[~街道和小区]龙域北街万科金域国际
[~单元和门牌]1603
[working_line]万科金域国际1603

```


王宇璐

Dec 3, 2016
