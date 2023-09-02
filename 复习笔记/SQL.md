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

# 查询进阶 - 关联查询 - cross join

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

















