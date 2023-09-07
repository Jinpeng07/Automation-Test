# **Linux**运维常用命令

## **1.** **文本操作**

### **cat**命令

连接多个文件并且打印到屏幕输出，或者重定向到指定文件中。

此命令常用于显示单个文件内容，或者将几个文件内容连接起来一起显示，还可以从标准输入中读取内

容并显示，生产环境中，它常与重定向或追加符号配合使用。

![image-20230907220336339](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230907220336339.png)

执行cat的完整命令生成test.txt文件内容

```shell
cat >test.txt<<EOF # 此处必须使用两个小于号，EOF表示结束标记，既读到EOF就结束
> hello world
> linux centos
> EOF # EOF必须成对出现，也可以使用其他的成对标签替换，结尾的EOF必须顶格编写
```

### **echo**命令

echo命令能将指定文本显示在Linux命令行上，或者通过重定向符写入到指定的文件中。

```
echo hello # 直接输出文本
echo 'hello' # 解压使用引号将内容括起来，单引号，双引号均可
echo -e "hello\tworld" #使用-e可以识别特殊字符
```

echo可以配合重定向符将内容输入到文件

“>”为重定向符号，表示清除原文件里面的所有内容，然后将内容追加到文件的末尾

“>>”为追加重定向符号，即追加内容到文件的尾部（文件的最后一行）。

将文本追加到某个文件中

```shell
echo "hello world" >>hello.txt #文件会被自动创建
```

### **grep**命令 - 筛选

grep命令是Linux系统中最重要的命令之一，其功能是从文本文件或管道数据流中筛选匹配的行及数据，如果配合正则表达式技术一起使用，则功能会更加强大

grep命令里面的匹配模式，都是你要获取的内容，它们既可以是普通的文字符号也可以是正则表达式，其语法格式

```shell
grep option pattern file
#     参数     模式   文件
```

![image-20230907220807142](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230907220807142.png)

使用grep过滤不包含lisi字符串的行（-v参数）

```shell
grep -v "lisi" test.txt
# grep的-v参数的作用是排除，默认是以行为单位排除包含参数后面所接内容的某些行。
```

使用grep命令显示过滤后的内容的行号

```shell
grep -n "wangwu" test.txt
```

-i不区分大小写

```shell
grep -i "WANGWU" test.txt
```

同时过滤两个不同的字符串

```shell
grep -E "zhangsan|lisi" test.txt
```

计算匹配的字符串的数量

```shell
grep -c "zhangsan" test.txt
```

过滤包含字母a的行

```shell
grep ".*a.*" test.txt
```

### **sed**：流编辑器 - 增删改查

sed是Stream Editor（字符流编辑器）的缩写，简称流编辑器。

ed是操作、过滤和转换文本内容的强大工具。sed的常用功能包含对文件实现快速增删改查（增加、删除、修改、查询），其中查询的功能中最常用的两大功能是过滤（过滤指定字符串）和取行（取出指定的行）。

语法格式

```shell
sed [选项] [sed内置命令字符] [输入文件]
```

![image-20230907221958227](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230907221958227.png)

测试文件内容

```shell
cat test.txt
I am zhangsan
I like badminton ball,billiard ball and chinese chess
my site is http://www.zhangsan.com
my telphone is 123456
```

输出test.txt第2-3行的内容

```shell
sed -n '2,3p' test.txt # -n取消默认输出，利用p控制显示的行
```

过滤出含有zhangsan字符串的行，sed命令的过滤功能，类似于grep的过滤，不同的是需要用双斜线将

需要过滤的字符串包含在中间。

```shell
sed -n '/zhangsan/p' test.txt
```

删除含有zhangsan字符串的行，sed命令的删除功能（d字符），默认不会修改文件，如果需要修改文

件，则要用-i参数配合。

```shell
sed '/zhangsan/d' test.txt

sed -i '/zhangsan/d' test.txt
```

删除指定的行。

```shell
sed -i '3d' test.txt # 删除第3行
sed -i '5,8d' test.txt #删除5-8行
```

















