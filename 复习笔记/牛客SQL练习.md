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
    (
        employees as e
        left join dept_emp as de on e.emp_no = de.emp_no
    )
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















