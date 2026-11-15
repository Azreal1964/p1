#DDl-数据库操作
# 查询：
# 查询所有数据库：
# show databases;
# 查询当前数据库：
# select database()；
# 常见当前数据库：
# create database[if not exists]数据库名[default charset字符集][collate排序规则]；
# 删除：
# drop database[if exists]数据库名;
# 使用：
# use 数据库名；

# 查询当前数据库所有表：
# show tables; 先通过use指令
# 查询表结构：
# desc 表名；
# 查询指定表的建表语句：
# show create table 表名；

# 表操作-创建：
# create table 表名（
#     字段1 字段1类型[comment 字段1注释]，
#     字段2 字段2类型[comment 字段2注释]，
#     字段3 字段3类型[comment 字段3注释]，
#     ......
#     字段n 字段n类型[comment 字段n注释]
# ）[comment 表注释]；

#MySQL中的数据类型：主要分为三类：数值类型 字符串类型 日期时间类型
#数值类型 ：tinyint（1 byte) 小整型数  smallint （2 byte)  med#iumint （3 byte)  int/integer （4 byte)大整型数  bigint （8 byte) 极大整型数
# flort （8 byte)单精度浮点数值   double（4 byte) 双精度浮点数值  decimal（8 byte) 小数值
#score  double(4,1) 总长度为：4  小数部分为：1 有负数：signed  没有负数：unsigned
#char 定长字符串：char（10）最大长度无论里面有多少都占用10个字符串：性能好   varchar 变长字符串：根据里面的实际存储量来定内存：性能较差
# tinyblob  不超过255个字符的二进制数据  tinytext  短文本字符串  blob
# 二进制形式的长文本字节数据  text  长文本数据  mediumblob  二进制中等长度文本数据  mediumtext中等长度文本数据
# longblob 二进制的极大文本数据  longblob  极大文本数据

#日期时间类型  date 日期值  time  时间或持续时间   year  年份值    datetime   混合时间和时间值  timestamp  混合日期，时间戳

#修改表：
#增加 alter table 表名 add 字段名 类型（长度）commit注释][约束]；
#修改数据类型 alter table 表名 modify 字段名 新数据类型（长度）  alter table 表名 change 旧字段名 新字段名 类型（长度）[commit 注释][约束]
#删除字段 alter table 表名 drop字段名；
#修改表名 alter table 表名 rename to 表名
#删除表名 drop table[if exists] 表名；
#删除指定表  truncate table 表名；

#DML
#给指定字段添加数据：insert into 表名（字段名1，字段名2，...） values（值1，值2，...）；
#给全部字段添加数据： insert into 表名 values（值1，值2，...）；
#批量添加数据： insert into 表名（字段名1，字段名2，...） values（值1，值2，...），（值1，值2，...），（值1，值2，...）；
#insert into 表名 values（值1，值2，...）,（值1，值2，...），（值1，值2，...）；

#修改数据 update 表名 set 字段名1 = 值1，...[where 条件]；
# 修改语句的条件可以有，也可以没有，如果没有条件，则会修改整张表的使用数据
#删除数据： delete from 表名 [where 条件]


#DQL：select
#编写顺序：select(4)   from(1)   where(2)   group by(3)   having(3)   order by(5)   limit(6)
#基本查询
#查询多个字段 ： select 字段1，字段2，字段3...from 表名；    select*from 表名；
#设置别名： select 字段1[as 别名1]，字段2[as 别名2]...from 表名；as 可以省略
#去除重复记录：select distinct 字段列表 from 表名：

#条件查询： select 字段列表 from 表名 where  条件列表；判定null值 is null    is not null
#在什么之间： between 最小值 and 最大值；
#in（数字，数字，数字...)
#模糊匹配 like ‘__’;   like '%x'; 一个下滑线代表一个字符

#聚合函数： select 聚合函数（字段列表） from 表名 where 条件；  null值不参与计算  count max min avg sum

#分组查询 ： select 字段列表 from 表名 [where 条件] group by 分组字段名 [having 分组后过滤条件]；
#执行时机不同：where 是分组之前 不满足条件不分组；having是分组之后进行过滤
#判断条件不同：where不能对聚合函数进行判断，而having可以。

#排序查询： select 字段列表 from 表名 order by 字段1 排序方法1，字段2，排序方法2；asc:升序 decs：降序
#第一个字段相同才会进行第二个字段排序

#分页查询： select 字段列表 from 表名 limit 起始索引，查询记录数  页码-1*展示记录数，每页展示的记录
#order by 在limit前面

#DQL 执行顺序


#DCL管理用户，控制数据库的访问权限
#查询用户： use mysql；  select *from user；
#创建用户：create user '用户名'@'主机名' identified by '密码'；'%'任意主机都可以访问
#修改用户密码： alter user '用户名'@'主机名' identified with MySQL_native_password by '新密码'；
#删除用户： drop user '用户名'@'主机名'

#权限控制 ：
#查询权限：show grants for '用户名'@'主机名'；
#授予权限： grant 权限列表 on 数据库名.表名 to '用户名'@'主机名'；
#撤销权限： revoke 权限列表 on 数据库名.表名 from '用户名'@'主机名'；

#函数：是指可以直接被另一段程序调用的程序或代码。
#字符串函数
#concat（s1,s2,...sn） 字符串拼接
# Lower(str) 将字符串全转为小写
# upper(str) 将字符串全转为大写
# lpad(str,n,pad) 左填充，用字符串pad对str的左边进行填充，达到n个字符串长度
# rpad(str,n,pad) 右填充，用字符串pad对str的左边进行填充，达到n个字符串长度
# trim(str) 去掉字符串头部尾部的空格
# substring(str,start,len) 返回字符串str从start位置起的len个长度的字符串、

#数组函数
# ceil  向上取整
# floor  向下取整
# mod   返回x/y的模
# rand()   返回0——1内的随机数
# round(x,y)  求参数x的四舍五入的值，保留y位小数

#日期函数
# curdate()     返回当前日期
# curtime()     返回当前时间
# now()     返回当前日期和时间
# year(date)        获取指定date年份
# month(date)        获取指定date月份
# day(date)        获取指定date日期
# date_add(date,interval expr type)      返回一个日期/时间值加上一个时间间隔expr后的时间值
# datediff(date1,date2)     返回起始时间date1 和 结束时间 data2 之间的天数 date1 - date2

#流程函数
# if(value,t,f)     如果values为Ture，则返回t，否则为f
# ifnull(value1,value2)     如果values1不为空，返回value1，否则返回value2
# case（列名） when [val1] then [res1]...elis[default] end      如果vall为Ture，返回res1,...否则返回default默认值
# case[expr] when [vall] then [rea1] ... else[default] end      如果expr的值等于vall，返回res1,...否则返回default默认值

#约束
#约束是作用于表中字段上的规则，用于限制存储在表中的数据
#目的：保证数据库中数据正确，有效性和完整性
# 非空约束：限制该字段不能为null    关键字：not null
# 唯一约束：保证该字段的使用数据都是唯一，不重复的     unique
# 主键约束：主键是一行数据的唯一标志，要求非空且唯一    primary key
# 默认约束： 保存数据时，如果未指定该字段的值，则采用默认值    default
# 检查约束： 保证字段满足某个条件    check
# 外键约束： 用来让两张表的数据数据之间建立连接，保证数据的一致性和完整性    foreign key
# 自动增长： auto_increment

#外键约束
#外键用来让两张表的数据之间建立连接，从而保证数据的一致性和完整性
# create rable 表名(
#     字段名 数据类型，
#     ...
#     [constraint] [外键名称] foreign key(外键字段名) references 主表(主表列名)
# );
# alter table 表名 add constraint 外键名称 foreign key(外键字段名) references 主表(主表列名);

#删除外键
# alter table 表名 drop foreign key 外键名称;

#删除/更新行为 ： no action   当在父表删除/更新对应记录时，首先检查该记录是否有对应外键，如果有则不允许删除/更新
#restrict 当在父表删除/更新对应记录时，首先检查该记录是否有对应外键，如果有则不允许删除/更新
#cascade  当在父表删除/更新对应记录时，首先检查该记录是否有对应外键，如果有，则也删除/更新外键在子表中的记录。
#set null 当在父表中删除对应记录时，首先检查该记录是否有对应外键，如果有则设置子表中该外键值为null (要求该外键允许取null)
#set default 父表有变更时，子表将外键列设置成一个默认的值(innodb不支持)

#alter table 表名 add constraint 外键名称 foreign key (外键字段) references 主表名(主表字段名) on update cascade on delete cascade on delete cascade

#多表查询
#select * from emp，dept where emp.dept_id = dept.id

#内连接:
#内连接查询语法
#隐式内连接 select 字段列表 from 表1，表2 where 条件...; 交集部分
#显式内连接 select 字段列表 from 表1 [inner] join 表2 on 连接条件...;

#外连接：
#左外连接 ：select 字段列表 from 表1 left [outer] join 表2 on条件...;  完全包含左表消息
#右外连接 ： select 字段列表 from 表1 right [outer] join 表2 on条件...;

#自连接
#select 字段列表 from 表A 别名 join 表A 别名B on条件...;

#子查询 ：称为嵌套查询，又称子查询
#select * form t1 where column1 = (select column1 from t2);
#子查询外部的语句可以是 insert/update/delete/select

#标量子查询
#子查询返回的结果是单个值（数字，字符串，日期等），最简单的形式，这种子查询成为标量子查询。
#常用的操作符： = <> >= < <=
#select * from emp where dept_id = (select id from dept where name = '销售部');

#列子查询
#子查询返回的结果是一列(可以是多行),这种子查询称为列子查询
#in，not in ，any ， some ， all
#select id from dept where name = '销售部' or '市场部';
#select * from emp where dept_id in (2,4);
#select * from emp where dept_id in (select id from dept where name = '销售部' or '市场部');


#行子查询
#子查询返回的结果是一行 ， 这种子查询称为行子查询。
#=,<>,in,not in
#select salary .managerid from emp where name = 'zwj'
#select * from emp where salary = 12500 and managerid = 1; // select * from emp where (salary,managerid) = (select salary .managerid from emp where name = 'zwj');

#表子查询
#子查询返回的结果是多行多列，这种子查询称为表子查询。
#常用操作符：in

#事务
#事务是一组操作的集合，他是一个不可分割的工作单位，事务会把所有的操作作为一个整体一起向系统提交或撤销操作的请求，即这些操作要么同时成功，要么同时失败。

#事务操作
#转账操作（张三给李四转账1000）
# 1.查询张三账户余额
# select * from account where name = ‘张三’
#
# 2.将张三账户-1000
# update account set money = money -1000 where name = ‘张三’
#抛出异常
#
# 3.将李四账户+1000
# update account set money = money +1000 where name = ‘李四’
#set @@autocommit=0；
#设置/查看事务提交方式
#select @@autocommit；
#set @@autocommit=0；手动提交

#提交事务：commit；

#回滚事务 rollback；一但出错

#开启事务 ： start transaction 或 begin

# 事务的四大特性
#原子性：事务是不可分割的最小操作单元，要么全部成功，要么全部失败
#一致性：事务完成时，必须是所有的数据都保持一致状态
#隔离性：数据库提供的隔离机制，保证事务在不受外界影响的独立环境下运行
#持久性：事务一旦提交回滚，他对数据库中的数据的改变是永久的

#并发事务问题
#脏读 ：一个事务读到另外一个事务还没有提交的数据
#不可重复读 ： 一个事务先后读取同一条记录，但两次读取到的数据不同，称之为不可重复读
#幻读：一个事务按照条件查询数据时，没有对应的数据行，但是在插入数据时，又发现这行数据已经存在，好像出现了幻影

#事务的隔离级别
#select @@transaction_isolation;
#设置事务隔离级别
# set [session|global] transaction isolation level {read uncommitted|read committed |repeatable read |serializable}







