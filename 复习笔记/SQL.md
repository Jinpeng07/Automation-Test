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



















