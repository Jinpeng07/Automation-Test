# Part1 -- 重点

# 基础语法 - 查询 - 全表查询

```
select * from students；

这样的 SQL 语句时，就是在进行全表查询，它会返回数据表中的所有行，让我们可以全面了解表中的数据。
```

# 基础语法 - 查询 - 选择查询

```
select name, gender from students;

使用"选择查询"来获取所有学生的姓名（name）和性别（gender）信息，SQL 语句如下：
```

# 基础语法 - 查询 - 别名

```
select name as 员工姓名, position as 职位名称 from employees;

我们使用 "别名" 来获取所有团队成员的姓名（name）和职位（position）信息，并为它们取别名为 员工姓名 和 职位名称
```

# 基础语法 - 查询 - 常量和运算

```
select order_id, unit_price, quantity, unit_price * quantity as total_amount from orders;

我们需要计算每个订单的总金额（total_amount），即商品单价（unit_price）乘以购买数量（quantity）


SQL 可以直接把常量作为列名，比如执行下列 SQL 语句：
select 200, '篮球' as hobby;
查询结果如下：
200	hobby
200	篮球
```

# 基础语法 - 条件查询 - where

```
select name, price, stock from products where stock <= 20;

where 子句的语法如下：

SELECT 列1, 列2, ...
FROM 表名
WHERE 条件;

其中，列1, 列2, ...是你要选择的列，可以是具体的列名，也可以是*表示选择所有列。表名是你要从中查询数据的表名。条件是指定的查询条件，可以使用比较运算符（如=、<、>等）、逻辑运算符（如AND、OR等）、IN 操作符、LIKE 操作符等来设置条件。
```

# 基础语法 - 条件查询 - 运算符

```
1）使用 "!=" 运算符筛选出 name 不是 '小张' 的员工：

-- SQL查询语句
select name, age, salary from employees where name != '小张';

2）使用 ">" 运算符筛选出工资高于 5500 的员工：

-- SQL查询语句
select name, age, salary from employees where salary > 5500;

3）使用 "BETWEEN" 运算符筛选出年龄在 25 到 30 之间的员工：

-- SQL查询语句
select name, age, salary from employees where age between 25 and 30;

4)指定针对某个列的多个可能值
SELECT * FROM student WHERE name IN ('张三','李四')
```

# 基础语法 - 条件查询 - 空值

```
在数据库中，有时候数据表的某些字段可能没有值，即为空值（NULL）。

空值表示该字段的值是未知的、不存在的或者没有被填写的。在SQL查询中，我们可以使用 "IS NULL" 和 "IS NOT NULL" 来判断字段是否为空值或非空值。

使用 "IS NULL" 来查询出入职日期未填写的员工：
-- SQL查询语句
select name, age from employees where hire_date is null;
```

# 基础语法 - 条件查询 - 模糊查询

```
在 LIKE 模糊查询中，我们使用通配符来代表零个或多个字符，从而能够快速地找到匹配的数据。
有如下 2 种通配符：
百分号（%）：表示任意长度的任意字符序列。
下划线（_）：表示任意单个字符。

我们使用 LIKE 模糊查询来找出姓名（name）中包含关键字 "张" 的员工信息：

-- SQL查询语句
select name, age, position from employees where name like '%张%';
-- 只查询以 "张" 开头的数据行
select name, age, position from employees where name like '张%';
-- 只查询以 "张" 结尾的数据行
select name, age, position from employees where name like '%张';

同理，可以使用 not like 来查询不包含某关键字的信息。
select name, score from student where name not like '%李%'
```

# 基础语法 - 条件查询 - 逻辑运算

```
在逻辑运算中，常用的运算符有：

AND：表示逻辑与，要求同时满足多个条件，才返回 true。
OR：表示逻辑或，要求满足其中任意一个条件，就返回 true。
NOT：表示逻辑非，用于否定一个条件（本来是 true，用了 not 后转为 false）


我们使用逻辑运算来找出姓名中包含关键字 "李" 且 年龄小于 30 岁的员工信息：

-- SQL查询语句
select name, age, salary from employees where name like '%李%' and age < 30;
```

# 基础语法 - 去重

```
在 SQL 中，我们可以使用 DISTINCT 关键字来实现去重操作。

我们使用DISTINCT关键字来找出不同的班级 ID：
-- SQL 查询语句
select distinct class_id from students;

除了按照单字段去重外，DISTINCT 关键字还支持根据多个字段的组合来进行去重操作，确保多个字段的组合是唯一的。
示例语法如下：
distinct 字段1, 字段2, 字段3, ...
(注意：是组合唯一！！！！！)
```

# 基础语法 - 排序

```
在 SQL 中，我们可以使用 ORDER BY 关键字来实现排序操作。ORDER BY 后面跟上需要排序的字段，可以选择升序（ASC）或降序（DESC）排列。

按照年龄升序（从小到大）：
select name, age from students order by age asc;

按照分数降序（从大到小）：
select name, score from students order by score desc;

在排序的基础上，我们还可以根据多个字段的值进行排序。当第一个字段的值相同时，再按照第二个字段的值进行排序，以此类推。
order by 字段1 [升序/降序], 字段2 [升序/降序], ...
select name, age, score from student order by score desc, age asc;
```

# 基础语法 - 截断和偏移

```
在 SQL 中，我们使用 LIMIT 关键字来实现数据的截断和偏移。(类似切片)

我们使用LIMIT关键字来进行分页查询：

-- LIMIT 后只跟一个整数，表示要截断的数据条数（一次获取几条）
select task_name, due_date from tasks limit 2;
-- LIMIT 后跟 2 个整数，依次表示从第几条数据（下标）开始、一次获取几条
select task_name, due_date from tasks limit 2, 2;

查询语句 1 结果，只获取了 2 条数据：
task_name	due_date
完成报告	2023-08-05
预约医生	2023-08-08

查询语句 2 结果，从下标为 2（第 3 条）数据的位置开始获取 2 条数据：
task_name	due_date
购买礼物	2023-08-10
安排旅行	2023-08-15

请编写一条 SQL 查询语句，从名为 student 的数据表中选择学生姓名（name）和年龄（age），按照年龄从小到大排序，从第 2 条数据开始、截取 3 个学生的信息。
select name, age from student order by age asc limit 1, 3;
```

# 基础语法 - 条件分支

```
条件分支 case when 是 SQL 中用于根据条件进行分支处理的语法。它类似于其他编程语言中的 if else 条件判断语句，允许我们根据不同的条件选择不同的结果返回。

使用 case when 可以在查询结果中根据特定的条件动态生成新的列或对现有的列进行转换。

使用条件分支 case when ，根据 name 来判断学生是否会说 RAP，并起别名为 can_rap
SELECT
  name,
  CASE WHEN (name = '鸡哥') THEN '会' ELSE '不会' END AS can_rap
FROM
  student;
  
查询结果：
name	can_rap
小明	    不会
鸡哥	    会
李华	    不会
王五	    不会
case when 支持同时指定多个分支，示例语法如下：
CASE WHEN (条件1) THEN 结果1
	   WHEN (条件2) THEN 结果2
	   ...
	   ELSE 其他结果 END
	   
将学生按照年龄划分为三个年龄等级（age_level）：60 岁以上为 "老同学"，20 岁以上（不包括 60 岁以上）为 "年轻"，20 岁及以下、以及没有年龄信息为 "小同学"。
返回结果应包含学生的姓名（name）和年龄等级（age_level），并按姓名升序排序。
SELECT name, CASE WHEN (age > 60) THEN '老同学' WHEN (age > 20) THEN '年轻' ELSE '小同学' END AS age_level FROM student ORDER BY name asc;
```

### 行转成列

```
张三	语文	58
张三	数学	59
张三	英语	68
李四	语文	78
李四	数学	98
李四	英语	56
王五	语文	58
王五	数学	54
王五	英语	53

SELECT
	name,
	sum(CASE subject WHEN '语文' THEN score ELSE 0 END) AS '语文',
	sum(CASE subject WHEN '数学' THEN score ELSE 0 END) AS '数学',
	sum(CASE subject WHEN '英语' THEN score ELSE 0 END) AS '英语',
	sum(score) AS total_score
FROM
	student
GROUP BY
	name
	
张三	58	59	68	185
李四	78	98	56	232
王五	58	54	53	165
```



# 函数 - 时间函数

```
常用的时间函数有：

-- 获取当前日期
SELECT DATE() AS current_date;

-- 获取当前日期时间
SELECT DATETIME() AS current_datetime;

-- 获取当前时间
SELECT TIME() AS current_time;

为了方便对比，放到同一个表格

current_date	current_datetime	current_time
2023-08-01	   2023-08-01 14:30:00	  14:30:00

还有很多时间函数，比如计算两个日期的相差天数、获取当前日期对应的毫秒数等，实际运用时自行查阅即可，此处不做赘述。
```

# 函数 - 字符串处理

```
在 SQL 中，字符串处理是一类用于处理文本数据的函数。它们允许我们对字符串进行各种操作，如转换大小写、计算字符串长度以及搜索和替换子字符串等。字符串处理函数可以帮助我们在数据库中对字符串进行加工和转换，从而满足不同的需求。

1）使用字符串处理函数 UPPER 将姓名转换为大写：
-- 将姓名转换为大写
SELECT name, UPPER(name) AS upper_name
FROM employees;

2）使用字符串处理函数 LENGTH 计算姓名长度：
-- 计算姓名长度
SELECT name, LENGTH(name) AS name_length
FROM employees;

3）使用字符串处理函数 LOWER 将姓名转换为小写：
-- 将姓名转换为小写并进行条件筛选
SELECT name, LOWER(name) AS lower_name
FROM employees;
```

# 函数 - 聚合函数

```
在 SQL 中，聚合函数是一类用于对数据集进行 汇总计算 的特殊函数。它们可以对一组数据执行诸如计数、求和、平均值、最大值和最小值等操作。聚合函数通常在 SELECT 语句中配合 GROUP BY 子句使用，用于对分组后的数据进行汇总分析。

常见的聚合函数包括：
COUNT：计算指定列的行数或非空值的数量。
SUM：计算指定列的数值之和。
AVG：计算指定列的数值平均值。
MAX：找出指定列的最大值。
MIN：找出指定列的最小值。

1）使用聚合函数 COUNT 计算订单表中的总订单数：(有几行)
SELECT COUNT(*) AS order_num
FROM orders;

查询结果：
order_num
4

2）使用聚合函数 COUNT(DISTINCT 列名) 计算订单表中不同客户的数量：
SELECT COUNT(DISTINCT customer_id) AS customer_num
FROM orders;

查询结果：
customer_num
3

3）使用聚合函数 SUM 计算总订单金额：
SELECT SUM(amount) AS total_amount
FROM orders;

查询结果：
total_amount
500
```

# 分组聚合 - 单字段分组

```
在 SQL 中，分组聚合是一种对数据进行分类并对每个分类进行聚合计算的操作。它允许我们按照指定的列或字段对数据进行分组，然后对每个分组应用聚合函数，如 COUNT、SUM、AVG 等，以获得分组后的汇总结果。

举个例子：某个学校可以按照班级将学生分组，并对每个班级进行统计。查看每个班级有多少学生、每个班级的平均成绩。这样我们就能够对学校各班的学生情况有一个整体的了解，而不是单纯看个别学生的信息。

在 SQL 中，通常使用 GROUP BY 关键字对数据进行分组。

1）使用分组聚合查询中每个客户的编号：

SELECT customer_id
FROM orders
GROUP BY customer_id;
查询结果：

customer_id
A001
A002
A003

2）使用分组聚合查询每个客户的下单数：

SELECT customer_id, COUNT(order_id) AS order_num
FROM orders
GROUP BY customer_id;
查询结果：

customer_id	order_num
A001	2
A002	1
A003	1


统计学生表中的班级编号（class_id）和每个班级的平均成绩（avg_score）。
SELECT class_id, AVG(score) AS avg_score FROM student GROUP BY class_id;
```

# 分组聚合 - 多字段分组

```
假设有一个订单表 orders，包含以下字段：order_id（订单号）、product_id（商品编号）、customer_id（客户编号）、amount（订单金额）。

数据如下：

order_id	product_id	customer_id	amount
1			1		A001		100
2			1		A002		200
3			1		A001		150
4			1		A003		50
5			2		A001		50
要查询使用多字段分组查询表中 每个客户 购买的 每种商品 的总金额，相当于按照客户编号和商品编号分组：

-- 查询每个班级每次考试的学生人数
SELECT customer_id, product_id, SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id, product_id;
查询结果：

customer_id	product_id	total_amount
A001	1	250
A001	2	50
A002	1	200
A003	1	50
```

# 分组聚合 - having 子句

```
在 SQL 中，HAVING 子句用于在分组聚合后对分组进行过滤。它允许我们对分组后的结果进行条件筛选，只保留满足特定条件的分组。

HAVING 子句与条件查询 WHERE 子句的区别在于，WHERE 子句用于在 分组之前 进行过滤，而 HAVING 子句用于在 分组之后 进行过滤。

1）使用 HAVING 子句查询订单数超过 1 的客户：

SELECT customer_id, COUNT(order_id) AS order_num
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 1;
查询结果：

customer_id	order_num
A001	2
2）使用 HAVING 子句查询订单总金额超过 100 的客户：

-- 查询总成绩超过200的班级
SELECT customer_id, SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 100;
查询结果：

customer_id	total_amount
A001	250
A002	200


统计学生表中班级的总成绩超过 150 分的班级编号（class_id）和总成绩（total_score）
SELECT class_id, SUM(score) AS total_score FROM student GROUP BY class_id HAVING SUM(score) > 150;
```

# 查询进阶 - 关联查询 - cross join 笛卡尔积

```
在 SQL 中，关联查询是一种用于联合多个数据表中的数据的查询方式。
其中，CROSS JOIN 是一种简单的关联查询，不需要任何条件来匹配行，它直接将左表的 每一行 与右表的 每一行 进行组合，返回的结果是两个表的笛卡尔积。

假设有一个员工表 employees，包含以下字段：emp_id（员工编号）、emp_name（员工姓名）、department（所属部门）、salary（工资）。数据如下：
emp_id	emp_name	department	salary
1	小明	技术部	5000
2	鸡哥	财务部	6000
3	李华	销售部	4500

假设还有一个部门表 departments，包含以下字段：department（部门名称）、manager（部门经理）、location（所在地）。数据如下：
department	manager	location
技术部	张三	上海
财务部	李四	北京
销售部	王五	广州

使用 CROSS JOIN 进行关联查询，将员工表和部门表的所有行组合在一起，获取员工姓名、工资、部门名称和部门经理，示例 SQL 代码如下：
SELECT e.emp_name, e.salary, e.department, d.manager
FROM employees e
CROSS JOIN departments d;

注意，在多表关联查询的 SQL 中，我们最好在选择字段时指定字段所属表的名称（比如 e.emp_name），还可以通过给表起别名（比如 employees e）来简化 SQL 语句。

查询结果：
emp_name	salary	department	manager
小明	5000	技术部	张三
小明	5000	财务部	李四
小明	5000	销售部	王五
鸡哥	6000	技术部	张三
鸡哥	6000	财务部	李四
鸡哥	6000	销售部	王五
李华	4500	技术部	张三
李华	4500	财务部	李四
李华	4500	销售部	王五
```

# 查询进阶 - 关联查询 - inner join 交集

```
在 SQL 中，INNER JOIN 是一种常见的关联查询方式，它根据两个表之间的关联条件，将满足条件的行组合在一起。

注意，INNER JOIN 只返回两个表中满足关联条件的交集部分，即在两个表中都存在的匹配行。

假设有一个员工表 employees，包含以下字段：emp_id（员工编号）、emp_name（员工姓名）、department（所属部门）、salary（工资）。数据如下：

emp_id	emp_name	department	salary
1	小明	技术部	5000
2	鸡哥	财务部	6000
3	李华	销售部	4500
假设还有一个部门表 departments，包含以下字段：department（部门名称）、manager（部门经理）、location（所在地）。数据如下：

department	manager	location
技术部	张三	上海
财务部	李四	北京
销售部	王五	广州
摸鱼部	赵二	吐鲁番

使用 INNER JOIN 进行关联查询，根据员工表和部门表之间的公共字段 部门名称（department） 进行匹配，将员工的姓名、工资以及所属部门和部门经理组合在一起：

SELECT e.emp_name, e.salary, e.department, d.manager
FROM employees e
JOIN departments d ON e.department = d.department;
查询结果如下：

emp_name	salary	department	manager
小明	5000	技术部	张三
鸡哥	6000	财务部	李四
李华	4500	销售部	王五
我们会发现，使用 INNER_JOIN 后，只有两个表之间存在对应关系的数据才会被放到查询结果中。
```

# 查询进阶 - 关联查询 - outer join 并集

```
在 SQL 中，OUTER JOIN 是一种关联查询方式，它根据指定的关联条件，将两个表中满足条件的行组合在一起，并 包含没有匹配的行 。

在 OUTER JOIN 中，包括 LEFT OUTER JOIN 和 RIGHT OUTER JOIN 两种类型，它们分别表示查询左表和右表的所有行（即使没有被匹配），再加上满足条件的交集部分。

假设有一个员工表 employees，包含以下字段：emp_id（员工编号）、emp_name（员工姓名）、department（所属部门）、salary（工资）。数据如下：

emp_id	emp_name	department	salary
1	小明	技术部	5000
2	鸡哥	财务部	6000
3	李华	销售部	4500
假设还有一个部门表 departments，包含以下字段：department（部门名称）、manager（部门经理）、location（所在地）。数据如下：

department	manager	location
技术部	张三	上海
财务部	李四	北京
人事部	王五	广州
摸鱼部	赵二	吐鲁番

使用 LEFT JOIN 进行关联查询，根据员工表和部门表之间的部门名称进行匹配，将员工的姓名、工资以及所属部门和部门经理组合在一起，并包含所有员工的信息：

SELECT e.emp_name, e.salary, e.department, d.manager
FROM employees e
LEFT JOIN departments d ON e.department = d.department;
查询结果：

emp_name	salary	department	manager
小明	5000	技术部	张三
鸡哥	6000	财务部	李四
李华	4500	销售部	NULL
关注下表格的最后一条数据，李华所属的销售部并没有在部门表中，但仍然返回在了结果集中，manager 为 NULL。

有些数据库并不支持 RIGHT JOIN 语法，那么如何实现 RIGHT JOIN 呢？

其实只需要把主表（from 后面的表）和关联表（LEFT JOIN 后面的表）顺序进行调换即可！
```

# 查询进阶 - 子查询

```
子查询是指在一个查询语句内部 嵌套 另一个完整的查询语句，内层查询被称为子查询。子查询可以用于获取更复杂的查询结果或者用于过滤数据。

当执行包含子查询的查询语句时，数据库引擎会首先执行子查询，然后将其结果作为条件或数据源来执行外层查询。

打个比方，子查询就像是在一个盒子中的盒子，外层查询是大盒子，内层查询是小盒子。执行查询时，我们首先打开小盒子获取结果，然后将小盒子的结果放到大盒子中继续处理。

假设我们有以下两个数据表：orders 和 customers，分别包含订单信息和客户信息。

orders 表：

order_id	customer_id	order_date	total_amount
1	101	2023-01-01	200
2	102	2023-01-05	350
3	101	2023-01-10	120
4	103	2023-01-15	500
customers 表：

customer_id	name	city
101	Alice	New York
102	Bob	Los Angeles
103	Charlie	Chicago
现在，我们希望查询出订单总金额 > 200 的客户的姓名和他们的订单总金额，示例 SQL 如下：

-- 主查询
SELECT name, total_amount
FROM customers
WHERE customer_id IN (
    -- 子查询
    SELECT DISTINCT customer_id
    FROM orders
    WHERE total_amount > 200
);
在上述 SQL 中，先通过子查询从订单表中过滤查询出了符合条件的客户 id，然后再根据客户 id 到客户信息表中查询客户信息，这样可以少查询很多客户信息数据。

上述语句的查询结果：

name	total_amount
Bob	350
Charlie	500
```

# 查询进阶 - 子查询 - exists

```
子查询中的一种特殊类型是 "exists" 子查询，用于检查主查询的结果集是否存在满足条件的记录，它返回布尔值（True 或 False），而不返回实际的数据。

假设我们有以下两个数据表：orders 和 customers，分别包含订单信息和客户信息。

orders 表：
order_id	customer_id	order_date	total_amount
1	101	2023-01-01	200
2	102	2023-01-05	350
3	101	2023-01-10	120
4	103	2023-01-15	500

customers 表：
customer_id	name	city
101	Alice	New York
102	Bob	Los Angeles
103	Charlie	Chicago
104	赵二	China

现在，我们希望查询出 存在订单的 客户姓名和订单金额。
使用 exists 子查询的方式，SQL 代码如下：

-- 主查询
SELECT name, total_amount
FROM customers
WHERE EXISTS (
    -- 子查询
    SELECT 1
    FROM orders
    WHERE orders.customer_id = customers.customer_id
);
上述语句中，先遍历客户信息表的每一行，获取到客户编号；然后执行子查询，从订单表中查找该客户编号是否存在，如果存在则返回结果。

查询结果如下：

name	total_amount
Alice	200
Bob	350
Charlie	500
和 exists 相对的是 not exists，用于查找不满足存在条件的记录。
```

# 查询进阶 - 组合查询

```
在 SQL 中，组合查询是一种将多个 SELECT 查询结果合并在一起的查询操作。

包括两种常见的组合查询操作：UNION 和 UNION ALL。

UNION 操作：它用于将两个或多个查询的结果集合并， 并去除重复的行 。即如果两个查询的结果有相同的行，则只保留一行。

UNION ALL 操作：它也用于将两个或多个查询的结果集合并， 但不去除重复的行 。即如果两个查询的结果有相同的行，则全部保留。

假设我们有以下两个数据表：table1 和 table2，分别包含不同部门的员工信息。

table1 表：
emp_id	name	age	department
101	Alice	25	HR
102	Bob	28	Finance
103	Charlie	22	IT

table2 表：
emp_id	name	age	department
101	Alice	25	HR
201	David	27	Finance
202	Eve	24	HR
203	Frank	26	IT

现在，我们想要合并这两张表的数据，分别执行 UNION 操作和 UNION ALL 操作。

UNION 操作：
SELECT name, age, department
FROM table1
UNION
SELECT name, age, department
FROM table2;
UNION 操作的结果，去除了重复的行（名称为 Alice）：

name	age	department
Alice	25	HR
Bob	28	Finance
Charlie	22	IT
David	27	Finance
Eve	24	HR
Frank	26	IT


-- UNION ALL操作
SELECT name, age, department
FROM table1
UNION ALL
SELECT name, age, department
FROM table2;
结果如下，保留了重复的行：
name	age	department
Alice	25	HR
Bob	28	Finance
Charlie	22	IT
Alice	25	HR
David	27	Finance
Eve	24	HR
Frank	26	IT
```

# 查询进阶 - 开窗函数 - sum over

```
在 SQL 中，开窗函数是一种强大的查询工具，它允许我们在查询中进行对分组数据进行计算、 同时保留原始行的详细信息 。

开窗函数可以与聚合函数（如 SUM、AVG、COUNT 等）结合使用，但与普通聚合函数不同，开窗函数不会导致结果集的行数减少。

打个比方，可以将开窗函数想象成一种 "透视镜"，它能够将我们聚焦在某个特定的分组，同时还能看到整体的全景。

假设我们有订单表 orders，表格数据如下：
order_id	customer_id	order_date	total_amount
1	101	2023-01-01	200
2	102	2023-01-05	350
3	101	2023-01-10	120
4	103	2023-01-15	500
现在，我们希望计算每个客户的订单总金额，并显示每个订单的详细信息。

示例 SQL 如下：

SELECT 
    order_id, 
    customer_id, 
    order_date, 
    total_amount,
    SUM(total_amount) OVER (PARTITION BY customer_id) AS customer_total_amount
FROM
    orders;
查询结果：

order_id	customer_id	order_date	total_amount	customer_total_amount
1	101	2023-01-01	200	320
3	101	2023-01-10	120	320
2	102	2023-01-05	350	350
4	103	2023-01-15	500	500
在上面的示例中，我们使用开窗函数 SUM 来计算每个客户的订单总金额（customer_total_amount），并使用 PARTITION BY 子句按照customer_id 进行分组。从前两行可以看到，开窗函数保留了原始订单的详细信息，同时计算了每个客户的订单总金额。
```

# 查询进阶 - 开窗函数 - sum over order by

```
sum over 函数的另一种用法：sum over order by，可以实现同组内数据的 累加求和 

举一个应用场景：老师在每个班级里依次点名，每点到一个学生，老师都会记录当前已点到的学生们的分数总和

假设我们有订单表 orders，表格数据如下：

order_id	customer_id	order_date	total_amount
1	101	2023-01-01	200
2	102	2023-01-05	350
3	101	2023-01-10	120
4	103	2023-01-15	500
现在，我们希望计算每个客户的历史订单累计金额，并显示每个订单的详细信息。

SELECT 
    order_id, 
    customer_id, 
    order_date, 
    total_amount,
    SUM(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date ASC) AS cumulative_total_amount
FROM
    orders;
    
结果将是：
order_id	customer_id	order_date	total_amount	cumulative_total_amount
1	101	2023-01-01	200	200
3	101	2023-01-10	120	320
2	102	2023-01-05	350	350
4	103	2023-01-15	500	500

在上面的示例中，我们使用开窗函数 SUM 来计算每个客户的历史订单累计金额（cumulative_total_amount），并使用 PARTITION BY 子句按照 customer_id 进行分组，并使用 ORDER BY 子句按照 order_date 进行排序。从结果的前两行可以看到，开窗函数保留了原始订单的详细信息，同时计算了每个客户的历史订单累计金额；相比于只用 sum over，同组内的累加列名称
```

# 查询进阶 - 开窗函数 - rank 不唯一的排名

```
Rank 开窗函数是 SQL 中一种用于对查询结果集中的行进行 排名 的开窗函数。它可以根据指定的列或表达式对结果集中的行进行排序，并为每一行分配一个排名。在排名过程中，相同的值将被赋予相同的排名，而不同的值将被赋予不同的排名。

Rank 开窗函数的常见用法是在查询结果中查找前几名（Top N）或排名最高的行。

Rank 开窗函数的语法如下：

RANK() OVER (
  PARTITION BY 列名1, 列名2, ... -- 可选，用于指定分组列
  ORDER BY 列名3 [ASC|DESC], 列名4 [ASC|DESC], ... -- 用于指定排序列及排序方式
) AS rank_column

其中，PARTITION BY 子句可选，用于指定分组列，将结果集按照指定列进行分组；ORDER BY 子句用于指定排序列及排序方式，决定了计算 Rank 时的排序规则。AS rank_column 用于指定生成的 Rank 排名列的别名。


假设我们有订单表 orders，表格数据如下：

order_id	customer_id	order_date	total_amount
1	101	2023-01-01	200
2	102	2023-01-05	350
3	101	2023-01-10	120
4	103	2023-01-15	500
现在，我们希望为每个客户的订单按照订单金额降序排名，并显示每个订单的详细信息。

SELECT 
    order_id, 
    customer_id, 
    order_date, 
    total_amount,
    RANK() OVER (PARTITION BY customer_id ORDER BY total_amount DESC) AS customer_rank
FROM
    orders;
查询结果：

order_id	customer_id	order_date	total_amount	customer_rank
1	101	2023-01-01	200	1
3	101	2023-01-10	120	2
2	102	2023-01-05	350	1
4	103	2023-01-15	500	1
在上面的示例中，我们使用开窗函数 RANK 来为每个客户的订单按照订单金额降序排名（customer_rank），并使用 PARTITION BY 子句按照 customer_id 进行分组，并使用 ORDER BY 子句按照 total_amount 从大到小进行排序。

可以看到，开窗函数保留了原始订单的详细信息，同时计算了每个客户的订单金额排名。
```

# 查询进阶 - 开窗函数 - row_number 唯一的排名

```
Row_Number 开窗函数是 SQL 中的一种用于为查询结果集中的每一行 分配唯一连续排名 的开窗函数。

它与之前讲到的 Rank 函数，Row_Number 函数为每一行都分配一个唯一的整数值，不管是否存在并列（相同排序值）的情况。每一行都有一个唯一的行号，从 1 开始连续递增。

比如说rank()是 1 1 3 4 4 6, 
row_number()就是1 2 3 4 5 6,
dense_rank() 就是 1 1 2 3 3 4
```

![image-20230903140957143](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230903140957143.png)

# 查询进阶 - 开窗函数 - lag / lead

```
开窗函数 Lag 和 Lead 的作用是获取在当前行之前或之后的行的值，这两个函数通常在需要比较相邻行数据或进行时间序列分析时非常有用。

1）Lag 函数

Lag 函数用于获取 当前行之前 的某一列的值。它可以帮助我们查看上一行的数据。

Lag 函数的语法如下：

LAG(column_name, offset, default_value) OVER (PARTITION BY partition_column ORDER BY sort_column)
参数解释：

column_name：要获取值的列名。
offset：表示要向上偏移的行数。例如，offset为1表示获取上一行的值，offset为2表示获取上两行的值，以此类推。
default_value：可选参数，用于指定当没有前一行时的默认值。
PARTITION BY和ORDER BY子句可选，用于分组和排序数据。////over()必须有!!!!
2）Lead 函数

Lead 函数用于获取 当前行之后 的某一列的值。它可以帮助我们查看下一行的数据。

Lead 函数的语法如下：

LEAD(column_name, offset, default_value) OVER (PARTITION BY partition_column ORDER BY sort_column)
参数解释：

column_name：要获取值的列名。
offset：表示要向下偏移的行数。例如，offset为1表示获取下一行的值，offset为2表示获取下两行的值，以此类推。
default_value：可选参数，用于指定当没有后一行时的默认值。
PARTITION BY和ORDER BY子句可选，用于分组和排序数据。


以下是一个示例，假设我们有一个学生成绩表scores，其中包含学生的成绩和考试日期：
student_id	exam_date	score
101	2023-01-01	85
101	2023-01-05	78
101	2023-01-10	92
101	2023-01-15	80
现在我们想要查询每个学生的考试日期和上一次考试的成绩，以及下一次考试的成绩，示例 SQL 如下：

SELECT 
    student_id,
    exam_date,
    score,
    LAG(score, 1, NULL) OVER (PARTITION BY student_id ORDER BY exam_date) AS previous_score,
    LEAD(score, 1, NULL) OVER (PARTITION BY student_id ORDER BY exam_date) AS next_score
FROM
    scores;
结果将是：

student_id	exam_date	score	previous_score	next_score
101	        2023-01-01	 85	           NULL	      78
101	        2023-01-05	 78	           85	      92
101	        2023-01-10	 92	           78	      80
101      	2023-01-15	 80	           92	      NULL
在上面的示例中，我们使用 Lag 函数获取每个学生的上一次考试成绩（previous_score），使用 Lead 函数获取每个学生的下一次考试成绩（next_score）。如果没有上一次或下一次考试，对应的列将显示为 NULL。
```

# Part2 -- 查缺补漏

## INSERT INTO 语句

```
INSERT INTO 语句可以有两种编写形式。

第一种形式无需指定要插入数据的列名，只需提供被插入的值即可：

INSERT INTO table_name
VALUES (value1,value2,value3,...);
第二种形式需要指定列名及被插入的值：

INSERT INTO table_name (column1,column2,column3,...)
VALUES (value1,value2,value3,...);
```

## UPDATE 语句

```
SQL UPDATE 语句
UPDATE 语句用于更新表中已存在的记录。

SQL UPDATE 语法
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;


Update 警告！
在更新记录时要格外小心！在上面的实例中，如果我们省略了 WHERE 子句，如下所示：

UPDATE Websites
SET alexa='5000', country='USA'
执行以上代码会将 Websites 表中所有数据的 alexa 改为 5000，country 改为 USA。

执行没有 WHERE 子句的 UPDATE 要慎重，再慎重。

在 MySQL 中可以通过设置 sql_safe_updates 这个自带的参数来解决，当该参数开启的情况下，你必须在update 语句后携带 where 条件，否则就会报错。
set sql_safe_updates=1; 表示开启该参数
```

## DELETE 语句

```
DELETE 语句用于删除表中的行。

SQL DELETE 语法
DELETE FROM table_name
WHERE condition;


删除所有数据
您可以在不删除表的情况下，删除表中所有的行。这意味着表结构、属性、索引将保持不变：

DELETE FROM table_name;
```

## SELECT TOP, LIMIT, ROWNUM 子句

```
SQL Server / MS Access 语法
SELECT TOP number|percent column_name(s)
FROM table_name;

变相返回后 N 行:
--前5行
select top 5 * from table
--后5行
select top 5 * from table order by id desc  --desc 表示降序排列 asc 表示升序

MySQL 语法
SELECT column_name(s)
FROM table_name
LIMIT number;

Oracle 语法
SELECT column_name(s)
FROM table_name
WHERE ROWNUM <= number;
```

## SQL 通配符

```
通配符	                        描述
%	                      替代 0 个或多个字符
_	                      替代一个字符
[charlist]	              字符列中的任何单一字符
[^charlist]或[!charlist]	 不在字符列中的任何单一字符

MySQL 中使用 REGEXP 或 NOT REGEXP 运算符 (或 RLIKE 和 NOT RLIKE) 来操作正则表达式。

下面的 SQL 语句选取 name 以 "G"、"F" 或 "s" 开始的所有网站：
SELECT * FROM Websites WHERE name REGEXP '^[GFs]';

下面的 SQL 语句选取 name 以 A 到 H 字母开头的网站：
SELECT * FROM Websites WHERE name REGEXP '^[A-H]';

下面的 SQL 语句选取 name 不以 A 到 H 字母开头的网站：
SELECT * FROM WebsitesWHERE name REGEXP '^[^A-H]';
```

## BETWEEN 操作符

```
带有文本值的 BETWEEN 操作符实例

下面的 SQL 语句选取 name 以介于 'A' 和 'H' 之间字母开始的所有网站：
SELECT * FROM WebsitesWHERE name BETWEEN 'A' AND 'H'; (name里的字母都要在A-H之间)
```

## FULL OUTER JOIN 关键字 MySQL中不支持 FULL OUTER JOIN

```
FULL OUTER JOIN 关键字结合了 LEFT JOIN 和 RIGHT JOIN 的结果。

SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2
ON table1.column_name=table2.column_name;
```

## UNION 操作符

```
UNION 只会选取不同的值。请使用 UNION ALL 来选取重复的值！

SELECT country, name FROM Websites WHERE country='CN'
UNION ALL
SELECT country, app_name FROM apps WHERE country='CN'ORDER BY country;
name做为第二列名
```

## SQL 拷贝

```
1. 复制表结构及其数据：
create table table_name_new as select * from table_name_old

2. 只复制表结构：
create table table_name_new as select * from table_name_old where 1=2;
或者：
create table table_name_new like table_name_old

3. 只复制表数据：
如果两个表结构一样：
insert into table_name_new select * from table_name_old

如果两个表结构不一样：
insert into table_name_new(column1,column2...) select column1,column2... from table_name_old
```

## SQL 约束（Constraints）

```
SQL CREATE TABLE + CONSTRAINT 语法
CREATE TABLE table_name
(
column_name1 data_type(size) constraint_name,
column_name2 data_type(size) constraint_name,
column_name3 data_type(size) constraint_name,
....
);

NOT NULL - 指示某列不能存储 NULL 值。
UNIQUE - 保证某列的每行必须有唯一的值。
PRIMARY KEY - NOT NULL 和 UNIQUE 的结合。确保某列（或两个列多个列的结合）有唯一标识，有助于更容易更快速地找到表中的一个特定的记录。
FOREIGN KEY - 保证一个表中的数据匹配另一个表中的值的参照完整性。
CHECK - 保证列中的值符合指定的条件。
DEFAULT - 规定没有给列赋值时的默认值。
```

### NOT NULL 约束

```
NOT NULL 约束强制列不接受 NULL 值。

添加 NOT NULL 约束
在一个已创建的表的 "Age" 字段中添加 NOT NULL 约束如下所示：
实例
ALTER TABLE Persons
MODIFY Age int NOT NULL;

删除 NOT NULL 约束
在一个已创建的表的 "Age" 字段中删除 NOT NULL 约束如下所示：
实例
ALTER TABLE Persons
MODIFY Age int NULL;
```

### UNIQUE 约束

```
UNIQUE 约束唯一标识数据库表中的每条记录。

UNIQUE 和 PRIMARY KEY 约束均为列或列集合提供了唯一性的保证。

PRIMARY KEY 约束拥有自动定义的 UNIQUE 约束。

请注意，每个表可以有多个 UNIQUE 约束，但是每个表只能有一个 PRIMARY KEY 约束。

MySQL：

CREATE TABLE Persons
(
P_Id int NOT NULL,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
UNIQUE (P_Id)
)
```

### PRIMARY KEY 约束

```
PRIMARY KEY 约束唯一标识数据库表中的每条记录。

主键必须包含唯一的值。

主键列不能包含 NULL 值。

每个表都应该有一个主键，并且每个表只能有一个主键。

MySQL：

CREATE TABLE Persons
(
P_Id int NOT NULL,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
PRIMARY KEY (P_Id)
)
```

### FOREIGN KEY 约束

```
FOREIGN KEY 约束用于预防破坏表之间连接的行为。

FOREIGN KEY 约束也能防止非法数据插入外键列，因为它必须是它指向的那个表中的值之一。

MySQL：

CREATE TABLE Orders
(
O_Id int NOT NULL,
OrderNo int NOT NULL,
P_Id int,
PRIMARY KEY (O_Id),
FOREIGN KEY (P_Id) REFERENCES Persons(P_Id)
)


alter table audit add foreign key (EMP_no) references employees_test (ID);
```

### CHECK 约束

```
CHECK 约束用于限制列中的值的范围。

如果对单个列定义 CHECK 约束，那么该列只允许特定的值。

如果对一个表定义 CHECK 约束，那么此约束会基于行中其他列的值在特定的列中对值进行限制。

CREATE TABLE Persons
(
P_Id int NOT NULL,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
CHECK (P_Id>0)
)
```

### DEFAULT 约束

```
DEFAULT 约束用于向列中插入默认值。

如果没有规定其他的值，那么会将默认值添加到所有的新记录。

CREATE TABLE Persons
(
    P_Id int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255) DEFAULT 'Sandnes'
)

当表已被创建时，如需在 "City" 列创建 DEFAULT 约束，请使用下面的 SQL：
MySQL：
ALTER TABLE Persons
ALTER City SET DEFAULT 'SANDNES'

如需撤销 DEFAULT 约束，请使用下面的 SQL：
MySQL：
ALTER TABLE Persons
ALTER City DROP DEFAULT
```

## CREATE INDEX

```
CREATE INDEX 语句用于在表中创建索引。

在不读取整个表的情况下，索引使数据库应用程序可以更快地查找数据。

SQL CREATE INDEX 语法
在表上创建一个简单的索引。允许使用重复的值：
CREATE INDEX index_name
ON table_name (column_name)

SQL CREATE UNIQUE INDEX 语法
在表上创建一个唯一的索引。不允许使用重复的值：唯一的索引意味着两个行不能拥有相同的索引值。
CREATE UNIQUE INDEX index_name
ON table_name (column_name)
注释：用于创建索引的语法在不同的数据库中不一样。因此，检查您的数据库中创建索引的语法。

下面的 SQL 语句在 "Persons" 表的 "LastName" 列上创建一个名为 "PIndex" 的索引：
CREATE INDEX PIndex
ON Persons (LastName)

alter table actor add unique index uniq_idx_firstname(first_name);
alter table actor add index idx_lastname(last_name);
```

## SQL 撤销索引、撤销表以及撤销数据库

```
DROP INDEX 语句用于删除表中的索引。
用于 MySQL 的 DROP INDEX 语法：
ALTER TABLE table_name DROP INDEX index_name

DROP TABLE 语句
DROP TABLE 语句用于删除表。
DROP TABLE table_name

DROP DATABASE 语句
DROP DATABASE 语句用于删除数据库。
DROP DATABASE database_name

TRUNCATE TABLE 语句
如果我们仅仅需要删除表内的数据，但并不删除表本身，那么我们该如何做呢？
请使用 TRUNCATE TABLE 语句：
TRUNCATE TABLE table_name
```

## ALTER TABLE 语句

```
ALTER TABLE 语句用于在已有的表中添加、删除或修改列。

如需在表中添加列，请使用下面的语法:
ALTER TABLE table_name
ADD COLUMN column_name datatype
ALTER TABLE actor ADD column create_date datetime NOT NULL  DEFAULT '2020-10-01 00:00:00' after last_update

如需删除表中的列，请使用下面的语法（请注意，某些数据库系统不允许这种在数据库表中删除列的方式）：
ALTER TABLE table_name
DROP COLUMN column_name

要改变表中列的数据类型，请使用下面的语法：
ALTER TABLE table_name
MODIFY COLUMN column_name datatype
```

## AUTO INCREMENT 字段

```
下面的 SQL 语句把 "Persons" 表中的 "ID" 列定义为 auto-increment 主键字段：

CREATE TABLE Persons
(
ID int NOT NULL AUTO_INCREMENT,
LastName varchar(255) NOT NULL,
FirstName varchar(255),
Address varchar(255),
City varchar(255),
PRIMARY KEY (ID)
)

MySQL 使用 AUTO_INCREMENT 关键字来执行 auto-increment 任务。
默认地，AUTO_INCREMENT 的开始值是 1，每条新记录递增 1。

要让 AUTO_INCREMENT 序列以其他的值起始，请使用下面的 SQL 语法：
ALTER TABLE Persons AUTO_INCREMENT=100
```

## SQL Date 函数

```
SELECT NOW(),CURDATE(),CURTIME()

DATE(date) date 参数是合法的日期表达式。

DATE_FORMAT(date,format) date 参数是合法的日期。format 规定日期/时间的输出格式。
下面的脚本使用 DATE_FORMAT() 函数来显示不同的格式。我们使用 NOW() 来获得当前的日期/时间：
DATE_FORMAT(NOW(),'%b %d %Y %h:%i %p')
DATE_FORMAT(NOW(),'%m-%d-%Y')
DATE_FORMAT(NOW(),'%d %b %y')
DATE_FORMAT(NOW(),'%d %b %Y %T:%f')

结果如下所示：
Nov 04 2008 11:45 PM
11-04-2008
04 Nov 08
04 Nov 2008 11:45:34:243

%a	缩写星期名
%b	缩写月名
%c	月，数值
%D	带有英文前缀的月中的天
%d	月的天，数值（00-31）
%e	月的天，数值（0-31）
%f	微秒
%H	小时（00-23）
%h	小时（01-12）
%I	小时（01-12）
%i	分钟，数值（00-59）
%j	年的天（001-366）
%k	小时（0-23）
%l	小时（1-12）
%M	月名
%m	月，数值（00-12）
%p	AM 或 PM
%r	时间，12-小时（hh:mm:ss AM 或 PM）
%S	秒（00-59）
%s	秒（00-59）
%T	时间, 24-小时（hh:mm:ss）
%U	周（00-53）星期日是一周的第一天
%u	周（00-53）星期一是一周的第一天
%V	周（01-53）星期日是一周的第一天，与 %X 使用
%v	周（01-53）星期一是一周的第一天，与 %x 使用
%W	星期名
%w	周的天（0=星期日, 6=星期六）
%X	年，其中的星期日是周的第一天，4 位，与 %V 使用
%x	年，其中的星期一是周的第一天，4 位，与 %v 使用
%Y	年，4 位
%y	年，2 位
```

## IFNULL()

```
MySQL 也拥有类似 ISNULL() 的函数。不过它的工作方式与微软的 ISNULL() 函数有点不同。

在 MySQL 中，我们可以使用 IFNULL() 函数，如下所示：
SELECT ProductName,UnitPrice*(UnitsInStock+IFNULL(UnitsOnOrder,0))
FROM Products

或者我们可以使用 COALESCE() 函数，如下所示：
SELECT ProductName,UnitPrice*(UnitsInStock+COALESCE(UnitsOnOrder,0))
FROM Products
```

# Part3 -- 函数

## SQL Aggregate 函数

```
SQL Aggregate 函数计算从列中取得的值，返回一个单一的值。

有用的 Aggregate 函数：

AVG() - 返回平均值 SELECT AVG(column_name) FROM table_name
COUNT() - 返回行数
FIRST() - 返回第一个记录的值  就是limit1
LAST() - 返回最后一个记录的值  就是Desc limit1
MAX() - 返回最大值
MIN() - 返回最小值
SUM() - 返回总和
```

### COUNT() - 返回行数

```
SQL COUNT(column_name) 语法
COUNT(column_name) 函数返回指定列的值的数目（NULL 不计入）：
SELECT COUNT(column_name) FROM table_name;

SQL COUNT(*) 语法
COUNT(*) 函数返回表中的记录数：
SELECT COUNT(*) FROM table_name;

SQL COUNT(DISTINCT column_name) 语法
COUNT(DISTINCT column_name) 函数返回指定列的不同值的数目：
SELECT COUNT(DISTINCT column_name) FROM table_name;
```

## SQL Scalar 函数

```
SQL Scalar 函数基于输入值，返回一个单一的值。

有用的 Scalar 函数：

- UPPER() - 将某个字段转换为大写    SELECT UPPER(column_name) FROM table_name;
- LOWER() - 将某个字段转换为小写    SELECT LOWER(column_name) FROM table_name;

- MID() - 从某个文本字段提取字符，MySql 中使用   
SELECT MID(name,1,4) AS ShortTitle FROM Websites;表示提取name中的1到4个字符
    
- LEN() - 返回某个文本字段的长度    SELECT LENGTH(column_name) FROM table_name;

- ROUND() - 对某个数值字段进行指定小数位数的四舍五入
SELECT ROUND(column_name,decimals) FROM TABLE_NAME; decimals可选表示留几位

- NOW() - 返回当前的系统日期和时间    SELECT NOW() FROM table_name;
- FORMAT() - 格式化某个字段的显示方式
SELECT name, url, DATE_FORMAT(Now(),'%Y-%m-%d') AS dateFROM Websites; 2020-02-02格式
```

## GROUP BY 多表连接

```
SELECT Websites.name,COUNT(access_log.aid) AS nums FROM access_log
LEFT JOIN Websites
ON access_log.site_id=Websites.id
GROUP BY Websites.name;
```

## EXISTS 运算符

```
EXISTS 运算符用于判断查询子句是否有记录，如果有一条或多条记录存在返回 True，否则返回 False。

SQL EXISTS 语法:
SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);
```
