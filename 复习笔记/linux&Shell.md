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

cat >>test.txt<<EOF 两个>意思是追加
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

### **sed**：流编辑器 - 增删改查 sed后面内置命令字符用单引号

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

将文件中的zhangsan字符串全部替换为lisi，sed命令的替换功能，默认不会修改文件，如果需要修改文

件，则要用-i参数配合，这个命令在工作中比较常用。

```shell
sed 's#zhangsan#lisi#g' test.txt
g表示全局替换，中间的间隔符号可以用 #@/ 等符号替代，前面表示需要替换的内容，后面表示替换后的内容
```

将文件中的zhangsan字符串全部替换为lisi，同时将telphone号码123456改为654321，sed命令的-e参数，多项编辑功能

```shell
sed -e 's#zhangsan#lisi#g' -e 's#123456#654321#g' test.txt
```

在test.txt文件的第2行后追加文本，sed命令的a字符功能

```shell
sed '2a hello' test.txt
```

也可以同时增加多行，不同的行之间使用“\n”间隔开

在test.txt文件的第2行插入文本，sed命令的i字符功能

```shell
sed -i '2i test' test.txt
```

**sed配合正则表达式的企业案例**

```
取出Linux中执行ifconfig eth0后对应的IP地址

方法1：利用正则加sed替换功能获取IP。
ifconfig ens33|sed -n '2s#^.*inet##gp'|sed -n 's#netm.*$##gp'

方法2：-e多项编辑可以减少管道的使用。
ifconfig ens33|sed -ne '2s#^.*inet ##g' -ne '2s#netm.*$##gp'
```

### **awk命令**

awk不仅仅是Linux系统中的一个命令，而且其还是一种编程语言，可以用来处理数据和生成报告（excel）。处理的数据可以是一个或多个文件，它是Linux系统最强大的文本处理工具，没有之一。awk的常用功能具体见表

![image-20230909153350301](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230909153350301.png)

```shell
awk [option] 'pattern{action}' file ...
awk [参数] '条件{动作}' file...
```

![image-20230909153429560](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230909153429560.png)

取test.txt文件的第2行到第3行的内容。

```shell
1. awk 'NR>1&&NR<4' #NR表达行号，&&表示并且

2. awk 'NR==2,NR==3' test.txt
```

过滤出含有root字符串的行，awk的过滤功能与sed的过滤功能类似，需要将要过滤的内容用两个斜线包含起来

```shell
awk '/root/' test.txt
```

取文件的第一列、第三列和最后一列的内容，并打印行号，awk的取列功能，这是awk的本行，即考察“$n”及NF、NR的用法。

```shell
awk -F ":" '{print NR,$1,$3,$NF}' test.txt

-F ":"表示以冒号为分隔符
print表示打印
$1是取分割后的第一列，NF表示最后一列，NR表示行号
```

取出Linux中执行ifconfig eth0后对应的IP地址, 利用多管道获取IP

```shell
ifconfig ens33|awk 'NR==2{print $2}'
# NR==2表示第2行，默认以空格作为分隔符，$2表示取出第二列
```

**处理以下文件内容，将域名取出并根据域名进行计数排序处理**

```shell
http://www.etiantian.org/index.html
http://www.etiantian.org/1.html
http://post.etiantian.org/index.html
http://mp3.etiantian.org/index.html
http://www.etiantian.org/3.html
http://post.etiantian.org/2.html

# 取出每行中的域名：
awk -F '/' '{print $3}' hosts.txt
# 排序（让相同的域名相邻）：
awk -F '/' '{print $3}' hosts.txt|sort
# 去重计数：
awk -F '/' '{print $3}' hosts.txt|sort|uniq -c
```

### 定时任务Cron(d)

在Linux系统中，Cron是定时任务的软件名，Crond是服务进程名，而crontab命令则是用来设置定时任务规则的配置命令，Cron定时任务人工划分为用户定时任务计划和系统定时任务计划两类：

1. 用户定时任务计划，Crond服务在工作时会以分钟为单位查看**/var/spool/cron**路径下以系统用户名命名的定时任务文件，以确定是否有需要执行的任务计划。如果有，就会将定时任务调度到内存中执行，使用crontab命令编辑的文件最终都会以当前用户名作为文件名存在于/var/spool/cron路径下。

2. 系统定时任务计划，Crond服务在工作时除了查看/var/spool/cron下的定时任务文件之外，还会查看/etc/cron.d目录以及/etc/anacrontab下的文件内容，里面通常是每天、每周或每月需要执行的任务

Crond服务除了执行用户定时任务计划（/var/spool/cron目录）以外，还会周期性地自动执行与操作系统相关的定时任务工作，例如轮询系统日志、备份系统数据、清理系统缓存等，这些任务无需我们人为干预。

![image-20230909160645946](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230909160645946.png)

使用crontab命令编辑的文件实际上就是在操作“/var/spool/cron/当前用户名”这样的文件

默认情况下，待用户建立定时任务规则之后，该规则所记录的对应配置文件将会存在于/var/spool/cron中，其crontab配置文件对应的文件名与登录的用户名应一致，例如，root用户的定时任务配置文件为/var/spool/cron/root。

利用crontab命令编写定时任务的书写格式很简单，规则一般可分为6个段（每个段之间均通过空格来分隔），前5段为时间设定段，第6段为所要执行的命令或脚本任务段。

```shell
分     时      日    月  周
00-59 00-23 01-31 01-12 0-7
01 * * * * cmd
02 4 * * * cmd
cmd为要执行的命令或脚本
每个列之间必须要有一个空格，可以存在多个空格。

* 每一秒
- 几秒到几秒
, 或
/n 隔几秒

*/2 * * * * /bin/sh /scripts/test.sh
# 第一列的意思为分钟，特殊符号“/”表示每隔的意思，即表示每隔2分钟执行一次test.sh程序。
30 3,12 * * * /bin/sh /scripts/test.sh
# 第一列为30，表示30分钟；第二列为“3，12”，表示3点和12点，此定时任务的意思是每天凌晨3：30和中
午12：30执行一脚本任务
30 */6 * * * /bin/sh /scripts/test.sh
# 第一列为30，表示30分钟；第二列“*/6”代表每6个小时，相当于就是6、12、18、24的作用。此定时任务
的意思是每隔6个小时的半点时刻执行一次脚本任务。
30 8-18/2 * * * /bin/sh /scripts/test.sh
# 其中的第一列为30，表示30分钟；第二列的“8-18/2”代表在早晨8点到下午18点之间每隔2小时，也相当
于是将8、10、12、14、16、18单独列出,此定时任务的意思就是早晨8点到下午18点之间，每隔2小时的半点
时刻执行一次脚本任务
30 21 * * * /opt/server/apache/bin/apachectl graceful
# 本例表示每晚的21：30重启Ap
```

**案例**

每天晚上0点，将站点目录/var/www/html下的内容打包备份到/data目录下，并且要求每次生成不同的备份包名。

```
# 备份数据，一般是采用压缩打包的形式
00 00 * * * /bin/tar zcf /data/bak_$(date +%F).tar.gz /var/www/html/
```

# Shell 概述

可通过以下命令查看CentOS系统的Shell支持情况。

```shell
cat /etc/shells
```

Linux系统中的主流Shell是bash, bash是由Bourne Shell（sh）发展而来的，同时bash还包含了csh和

ksh的特色。

查看CentOS Linux系统默认的Shell。

```shell
echo $SHELL

grep root /etc/passwd
# 结尾的/bin/bash就是用户登录后的Shell解释器
```

## Shell脚本的建立和执行

在Linux系统中，Shell脚本（bash Shell程序）通常是在编辑器vi/vim中编写的，由Shell命令、程序结构控制语句和注释等内容组成。

**脚本开头**

```shell
一个规范的Shell脚本在第一行会指出由哪个程序（解释器）来执行脚本中的内容，这一行内容在Linux 
bash的编程一般为：
#!/bin/bash

sh为bash的软链接，大多数情况下，脚本的开头使用“#!/bin/bash”和“#! /bin/sh”是没有区别的，但更规
范的写法是在脚本的开头使用“#! /bin/bash”
CentOS和Red Hat Linux下默认的Shell均为bash。因此，在写Shell脚本的时候，脚本的开头即使不加
“#! /bin/bash”，它也会交给bash解释
```

**Shell脚本的执行**

```shell
Shell脚本是从上至下依次执行每一行的命令及语句的，即执行完了一个命令后再执行下一个，如果在Shell脚本中遇到子脚本（即脚本嵌套）时，就会先执行子脚本的内容，完成后再返回父脚本继续执行父脚本内后续的命令及语句

通常情况下，在执行Shell脚本时，会向系统内核请求启动一个新的进程，以便在该进程中执行脚本的命令及子Shell脚本

Shell脚本的执行通常可以采用以下几种方式
1. bash script-name或sh script-name：这是当脚本文件本身没有可执行权限（即文件权限属性x位
为-号）时常使用的方法，或者脚本文件开头没有指定解释器时需要使用的方法。
bash script-name

2. path/script-name或 ./script-name：指在当前路径下执行脚本（脚本需要有执行权限），需要将脚本文件的权限先改为可执行（即文件权限属性加x位），具体方法为chmod +x script-name。然后通过脚本绝对路径或相对路径就可以直接执行脚本了
./script-name

3. source script-name或．script-name：这种方法通常是使用source或“.”（点号）读入或加载指定的Shell脚本文件，然后，依次执行指定的Shell脚本文件san.sh中的所有语句。这些语句将在当前父Shell脚本father.sh进程中运行（其他几种模式都会启动新的进程执行子脚本）
source script-name

使用source或“.”可以将自身脚本中的变量值或函数等的返回值传递到当前父Shell脚本father.sh中
使用。这是它和其他几种方法最大的区别
```

# Shell 变量

注意”=“的两侧无空格，否则变量名称会被识别为命令，变量的内容一般要加双引号，以防止出错，特别是当值里的内容之间有空格时。

默认情况下，在bash Shell中是不会区分变量类型的

## **子进程Shell与变量的可见性**

![image-20230909202531859](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230909202531859.png)

## **变量的类型**

变量可分为两类：环境变量（全局变量）和普通变量（局部变量）。

环境变量也可称为全局变量，可以在创建它们的Shell及其派生出来的任意子进程Shell中使用，环境变量又可分为自定义环境变量和bash内置的环境变量。

普通变量也可称为局部变量，只能在创建它们的Shell函数或Shell脚本中使用。普通变量一般由开发者在开发脚本程序时创建。

## **环境变量**

环境变量一般是指用export内置命令导出的变量，用于定义Shell的运行环境，保证Shell命令的正确执行。

环境变量可以在命令行中设置和创建，但用户退出命令行时这些变量值就会丢失，因此，如果希望永久保存环境变量，可在以下位置配置：

用户家目录下的．**bash_profile**或．bashrc（非用户登录模式特有，例如远程SSH）文件中

全局配置/etc/bashrc（非用户登录模式特有，例如远程SSH）或**/etc/profile**文件中定义。

在将环境变量放入上述的文件中后，每次用户登录时这些变量都将被初始化。

按照系统规范，所有环境变量的名字均采用大写形式。在将环境变量应用于用户进程程序之前，都应该用export命令导出定义，例如：正确的环境变量定义方法为

```shell
export FLAG=1  不加$
```

有一些环境变量，比如HOME、PATH、SHELL、UID、USER等，在用户登录之前就已经被/bin/login程序设置好了。通常环境变量被定义并保存在用户家目录下的．bash_profile文件或全局的配置文件/etc/profile中.

```
查看环境变量 env
显示当前 Shell 中所有变量 set
显示与取消环境变量 unset USER

常见系统环境变量：
$HOME：用户登录时进入的目录。
$UID：当前用户的UID（用户标识）
$PWD：当前工作目录的绝对路径名
$SHELL：当前SHELL。
$USER：当前用户
```

## **普通变量**

```shell
a=192.168.1.10-$a
b='192.168.1.10-$a'
c="192.168.1.10-$a"
echo "a=$a"
echo "b=$b"
echo "c=${c}"

输出如下:
a=192.168.1.10- 不输出
b=192.168.1.10-$a 原样输出
c=192.168.1.10-192.168.1.10- 解析后输出
```

# Shell 变量进阶

##  **1.** **将命令结果赋值给变量**

```shell
对需要获取命令结果的变量内容赋值的常见方法有两种：
变量=`ls`
变量=$(ls) 常用
```

## **2.特殊变量**

![image-20230909212457982](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230909212457982.png)

**$n**

```shell
echo $1 $2
bash p.sh hello world

在脚本中快速生成多个变量
echo \${1..15} #相当于 echo $1 ... $15

生成26个英文字母
echo {a..z}
bash p.sh {a..z} # 传入英文字母
```

**$0**

```shell
$0的作用为取出执行脚本的名称（包括路径）

不带路径执行脚本，那么输出结果就是脚本的名字，若使用全路径执行脚本，那么输出结果就是全路径
加上脚本的名字

此时如果希望单独获取名称或路径，则可用dirname及basename命令
dirname /opt/server/a.txt
basename /opt/server/a.txt
```

**$#**

```
通过$#获取脚本传参的个数

bash q.sh {a..z}
26
```

**$和$@**

```shell
测试$*和$@，注意，此时不带双引号：
echo $*
echo $@
for i in $*; do echo $i; done
for i in $@; do echo $i;
结果一样，都是一个一个输出

测试"$*"和"$@"，注意，此时带有双引号：
echo "$*"
echo "$@"
for i in "$*"; do echo $i; done 一行输出，当作一个元素
for i in "$@"; do echo $i; done 还是一个一个输出
```

**$?**

```
$?用于获取执行上一个指令的执行状态返回值，0表示成功，非0表示失败

mkdir a
echo $0 0
mkdir a
echo $0 1
```

## **3.**内置变量命令

```shell
echo
echo在屏幕上输出信息

eval
eval，当Shell程序执行到eval语句时，Shell读入参数args，并将它们组合成一个新的命令，然后执行。
命令格式：

bash noeval.sh arg1 arg2 
eval "echo \$$#"  #加上eval命令后，使得打印的特殊位置参数重新解析输出，而不是输出$2本身
```

# Shell 运算符

## 算术运算

### (())数值运算

```shell
双小括号“(())”的作用是进行数值运算与数值比较，它的效率很高，用法灵活，是企业场景运维人员经常
采用的运算操作符

echo $((1+1)) # 2
i=5
((i=i*2)) # 对i乘2，再赋值给i，此时没有输出，在“(())”中使用变量时可以去掉变量前的$符号。
echo $i
((a=1+2**3-10))
echo $a
b=$((1+2*3))
echo $b
echo $((1+10)) # 注意不能缺少$
echo $((a+=1))

利用“(())”双括号进行比较及判断。
echo $((8>10)) # 输出结果为0或1
echo $((8==8&&3>2))
```

上面涉及的数字及变量必须为整数（整型），不能是小数（浮点数）或字符串

(())”表达式在命令行执行时不需要加$符号，直接使用((6%2))形式即可，但是如果需要输出，就要加$符，例如：echo $((6%2))

(())”里的所有字符之间没有空格、有一个或多个空格都不会影响结果

### **let**运算命令

```shell
let 赋值表达式
let赋值表达式的功能等同于“((赋值表达式))”。

i=2
i=i+8 # 不使用let进行赋值
echo $i # i+8
unset i
i=2
let i=i+8 # 使用let赋值  let i=i+8等同于((i=i+8))，但后者效率更高。
echo $i
```

### **expr**命令

expr（evaluate（求值）expressions（表达式））命令既可以用于整数运算，也可以用于相关字符串长度、匹配等的运算处理

```shell
expr用于计算
expr 2 + 2
expr 10 \* 5
要注意，在使用expr时:
运算符及用于计算的数字左右都至少有一个空格，否则会报错。
使用乘号时，必须用反斜线屏蔽其特定含义，因为Shell可能会误解星号的含义。

expr在Shell中可配合变量进行计算，但需要用反引号将计算表达式括起来。
i=10
i=`expr $i + 6` ``的意思应该是把它当作表达式，而不是字符串
echo $i
```

### awk实现计算

```shell
利用awk进行运算的效果也很好，适合小数和整数，特别是命令行计算，尤其是小数，运算很精确，好
用

echo "7.5 2.5" | awk '{print ($1-$2)}' # $1为第一个数字，$2为第2个数字，用空格隔开
```

## **条件测试**

![image-20230909223953342](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230909223953342.png)

### **test**条件测试

```shell
test ＜测试表达式＞

test -f file && echo true || echo false
该语句表示如果file文件存在，则输出true，否则（||）输出false，这里的&&是并且的意思。test的-f参数用于测试文件是否为普通文件，test命令若执行成功（为真），则执行&&后面的命令，而||后面的命令是test命令执行失败之后（为假）所执行的命令。
```

### []（中括号）条件测试

```shell
[ ＜测试表达式＞ ]

中括号内部的两端要有空格，[]和test等价，即test的所有判断选项都可以直接在[]里使用。
[ -f /tmp/xx ] && echo 1 || echo 0
```

### **[[]]**条件测试

```shell
[[ ＜测试表达式＞ ]]

双中括号里的两端也要有空格
[[ -f /tmp/xx ]] && echo 1 || echo 0

在[[ ]]中可以使用通配符等进行模式匹配；并且&&、||、＞、＜等操作符可以应用于[[ ]]中，但不能应
用于[ ]中，在[ ]中一般使用-a、-o、-gt（用于整数）、-lt（用于整数）等操作符代替上文提到的用于[[]]
中的符号。
```

### **文件测试表达式**

![image-20230909224357338](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230909224357338.png)

### **字符串测试操作符**

![image-20230909224435361](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230909224435361.png)

### **整数二元比较操作符**

![image-20230909224535581](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230909224535581.png)

![image-20230909224630532](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230909224630532.png)

### **逻辑操作符**

![image-20230909224701783](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230909224701783.png)

### 测试表达式test、[]、[[]]、(())的区别总结

![image-20230909224737175](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230909224737175.png)

# **选择语句**

## **1. if**语句基本语法

### **单分支结构**

```shell
if [ -f "$file1" ];then
 echo 1
fi
```

### **双分支结构**

```shell
if [ -f "$file1" ]
   then
     echo 1
else
     echo 0
fi
```

### **多分支结构**

```
#! /bin/bash
if [ $1 -gt 20 ];then
    echo 20
elif [ $1 -gt 15 ];then
     echo 15
elif [ $1 -gt 10 ];then
     echo 10
else
     echo 0
fi

注意多分支elif的写法，每个elif都要带有then。
最后结尾的else后面没有then。
```

## **2. read**命令

Shell变量除了可以直接赋值或脚本传参外，还可以使用read命令从标准输入中获得，read为bash内置命令，可通过help read查看帮助

```shell
read [参数] [变量名]

常用参数如下。
-p prompt：设置提示信息。
-t timeout：设置输入等待的时间，单位默认为秒。

read -t 10 -p "input a number:" num # 变量前需要有空格
echo $num
read -t 10 -p "input two number:" num1 num2 # 变量前需要有空格
echo $num1 $num2

案例实操，使用read读入数字比较两个整数的大小，创建脚本文件 if.sh
read -p "input two number": a b
if [ $a -lt $b ]; then
 echo "$a < $b"
elif [ $a -eq $b ]; then
 echo "$a = $b"
else
 echo "$a > $b"
fi
```

### 3.case语句

```shell
read -p "input a number:" num
case "$num" in
 1)
   echo "the num is 1"
   ;;
 2)
   echo "the num is 2"
   ;;
 [3-9]) # 支持正则表达式
   echo "the num is $num"
   ;;
 *)
   echo "error"
esac
```









