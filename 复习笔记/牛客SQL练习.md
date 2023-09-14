**SQL196** **查找入职员工时间排名倒数第三的员工所有信息**

```
注意：可能会存在同一个日期入职的员工，所以入职员工时间排名倒数第三的员工可能不止一个。

select * from employees 
where hire_date = (
    select distinct hire_date from employees order by hire_date desc limit 2,1
)
```

**SQL206** **获取每个部门中当前员工薪水最高的相关信息**

```
先表关联，再借用开窗函数，使能用排名函数，获取rank为1的值
select
    t.dept_no,
    t.emp_no,
    t.salary as maxSalary
from
    (
        select
            d.dept_no,
            d.emp_no,
            s.salary,
            row_number() over (
                partition by
                    d.dept_no
                order by
                    s.salary desc
            ) as 'rank'
        from
            dept_emp d
            inner join salaries s on d.emp_no = s.emp_no
    ) as t
where
    t.rank = 1
```

**SQL212** **获取当前薪水第二多的员工的emp_no以及其对应的薪水salary**  -- **不能使用order by完成**

```
解法1 max 任意相同工资人数
select e.emp_no,s.salary,e.last_name,e.first_name
from
employees e
join 
salaries s on e.emp_no=s.emp_no 
and s.salary = (
			    //最高工资之外取最高的就是第二高的
				select max(salary)
                from salaries
                where salary<(
                			  //获取最高的工资	
                			  select max(salary) 
                              from salaries 
                             )
                )


第二种 通用型可以求任意第几高，并且可以求多个相同工资
select e.emp_no,s.salary,e.last_name,e.first_name
from
employees e
join 
salaries s on e.emp_no=s.emp_no 
and s.salary = 
(
     select s1.salary
     from 
     salaries s1
     join
     salaries s2 on s1.salary<=s2.salary 
     group by s1.salary
     having count(distinct s2.salary)=2
 )

```

**SQL213** **查找所有员工的last_name和first_name以及对应的dept_name**

```
三张表联合查询
#1
select
    e.last_name,
    e.first_name,
    d.dept_name
from
    employees as e
    left join dept_emp as de on e.emp_no = de.emp_no
    left join departments d on de.dept_no = d.dept_no
    
#2
select
    t.last_name,
    t.first_name,
    d.dept_name
from
    (
        select
            e.last_name,
            e.first_name,
            de.dept_no
        from
            employees as e
            left join dept_emp as de on e.emp_no = de.emp_no
    ) t
    left join departments d on t.dept_no = d.dept_no
```

**SQL228** **批量插入数据**

```
insert into 表名 values(数据1),(数据2)

insert into
    actor
values
    (1, 'PENELOPE', 'GUINESS', '2006-02-15 12:34:33'),
    (2, 'NICK', 'WAHLBERG', '2006-02-15 12:34:33')
```

**SQL229 批量插入数据，不使用replace操作**

```
# mysql中常用的三种插入数据的语句: 
# insert into表示插入数据，数据库会检查主键，如果出现重复会报错； 
# replace into表示插入替换数据，需求表中有PrimaryKey，
#             或者unique索引，如果数据库已经存在数据，则用新数据替换，如果没有数据效果则和insert into一样； 
# insert ignore表示，如果中已经存在相同的记录，则忽略当前新数据；
insert ignore into actor values("3","ED","CHASE","2006-02-15 12:34:33");
```

**SQL232** **针对actor表创建视图actor_name_view**

```
方法一：
create view actor_name_view as
select first_name as first_name_v, last_name as last_name_v
from actor

方法二：直接在视图名的后面用小括号创建视图中的字段名
create view actor_name_view(first_name_v, last_name_v) as
select first_name, last_name
from actor
```

![image-20230905205359841](C:\Users\Jinpeng\AppData\Roaming\Typora\typora-user-images\image-20230905205359841.png)

**SQL233** **针对上面的salaries表emp_no字段创建索引idx_emp_no**

```
使用强制索引
select * from salaries force index(idx_emp_no ) where emp_no=10005
```

**SQL238** **将id=5以及emp_no=10001的行数据替换成id=5以及emp_no=10005**

```
使用replace替换记录的语句为 replace(字段，旧内容，新内容)
结合update使用：
update titles_test
set emp_no=replace(emp_no,10001,10005)
where id=5;
```

**修改表名**

```
alter table titles_test rename titles_2017
```

**SQL244** **将employees表中的所有员工的last_name和first_name通过单引号连接起来**

```
方式一
select concat(last_name,'\'',first_name) from employees
方式二
select concat(last_name,"'",first_name) from employees
```

**SQL245** **查找字符串中逗号出现的次数**

```sql
select id,length(string)-length(replace(string,",","")) from strings;

SELECT
    id,
    length(
        regexp_replace(STRING, '[A-Z0-9]', '')
    )
FROM
    strings;
```

**SQL246** **获取employees中的first_name**

```sql
本题考查 substr(X,Y,Z) 或 substr(X,Y) 函数的使用。其中**X是要截取的字符串**。**Y是字符串的起始位置**（注意第一个字符的位置为1，而不为0），取值范围是±(1~length(X))，当Y等于length(X)时，则截取最后一个字符；当Y等于负整数-n时，则从倒数第n个字符处截取。**Z是要截取字符串的长度**，取值范围是正整数，若Z省略，则从Y处一直截取到字符串末尾；若Z大于剩下的字符串长度，也是截取到字符串末尾为止。

SELECT first_name FROM employees ORDER BY substr(first_name,length(first_name)-1) 
SELECT first_name FROM employees ORDER BY substr(first_name,-2) 
```

**SQL247** **按照dept_no进行汇总**

```sql
聚合函数group_concat（X，Y），其中X是要连接的字段，Y是连接时用的符号，可省略，默认为逗号。
此函数必须与GROUP BY配合使用。此题以dept_no作为分组，将每个分组中不同的emp_no用逗号连接起来（即可省略Y）。

SELECT dept_no,group_concat(emp_no) as employees
FROM dept_emp GROUP BY dept_no
```

**SQL249** **分页查询employees表，每5行一页，返回第2页的数据**

```sql
根据题意，每行5页，返回第2页的数据，即返回第6~10条记录，以下有两种方法可以解决：
方法一：利用 LIMIT 和 OFFSET 关键字。LIMIT 后的数字代表返回几条记录，OFFSET 后的数字代表从第几条记录开始
SELECT * FROM employees LIMIT 5 OFFSET 5

方法二：只利用 LIMIT 关键字。注意：在 LIMIT X,Y 中，Y代表返回几条记录，X代表从第几条记录开始返回（第一条记录序号为0），切勿记反。
SELECT * FROM employees LIMIT 5,5

拓展：若每页显示n条记录，要显示第i页数据，则可以用 limit n*(i-1),n 
n*(i-1)要算出来
```

**SQL259 异常的邮件概率**

```sql
select
    e.date,
    round(
        sum + case when 语句统计个数
        sum(
            case
                e.type
                when 'no_completed' then 1
                else 0
            end
        ) / count(*),
        3
    )
from
    email e
    inner join user u1 on e.send_id = u1.id
    and u1.is_blacklist = 0
    inner join user u2 on e.receive_id = u2.id
    and u2.is_blacklist = 0
group by
    e.date
order by
    e.date
```

**SQL261** **牛客每个人最近的登录日期(二)**

```sql
select
    u.name as u_n,
    c.name as c_n,
    lg.date as date
from
    login lg
    inner join user u on lg.user_id = u.id
    inner join client c on lg.client_id = c.id
where 注意这个用法
    (lg.user_id, lg.date) in (
        select
            user_id,
            max(date)
        from
            login
        group by
            user_id
    )
order by
    u_n
```

floor向下取整, ceil向上取整

**日期函数格式转换**

```sql
DATE_FORMAT(``date``,format)

常用格式	对应描述
%Y	--年，4 位
%m	--月，数值（00-12）
%M	--月名
%k	--小时（0-23）
```

**SQL282** **最差是第几名(二) **正序和和逆序和求中位数

```sql
当某一数的正序和逆序累计均大于整个序列的数字个数的一半即为中位数

select
    grade
from
    (
        select
            grade,
            (
                select
                    sum(number)
                from
                    class_grade
            ) as total,
            sum(number) over (
                order by
                    grade
            ) a,
            sum(number) over (
                order by
                    grade desc
            ) b
        from
            class_grade
    ) t1
where
    a >= total / 2       正序和12，大于等于6的，为C,D，
    and b >= total / 2   逆序和为12，大于等于6的为ABC，所以最后中位数为C
order by
    grade;

```

**SQL284** **获得积分最多的人(二)**

```
创建临时表语法
with
    temp_table as (
        select
            u.id,
            u.name,
            t.gsum
        from
            user u
            inner join (
                select
                    user_id,
                    sum(grade_num) as gsum
                from
                    grade_info
                group by
                    user_id
            ) t on u.id = t.user_id
        order by
            u.id desc
    )
select
    id,
    name,
    gsum
from
    temp_table
where
    gsum = (
        select
            max(gsum)
        from
            temp_table
    )
order by
    id
```

```
遇到排名第几的问题可以用开窗函数rank denserank等等，也可以用where = 具体的值
```

```
1.添加列
alter table 表名 add column 列名 类型 【first|after 字段名】;
2.修改列的类型或约束
alter table 表名 modify column 列名 新类型 【新约束】;
3.修改列名
alter table 表名 change column 旧列名 新列名 类型;
4 .删除列
alter table 表名 drop column 列名;
5.修改表名
alter table 表名 rename 【to】 新表名;
6.将某一列放到第一列
alter table 表名 modify column 列名 类型 first;
```











