## 课程笔记

#### 上课视频
1. [week3-database-and-design](https://www.jianguoyun.com/p/DZL0Ey4Q1YDIBxji4s4B)
2. [week3-data-visualization](https://www.jianguoyun.com/p/DYAWftIQ6LTJBxjfxswB)
3. data-model-design-ppt (materials/data-modeling.ppt)
4. matplotlib.ipynb/pandas-2-groupby_time_series.ipynb 下半部分课程材料

#### Principle 3: Abstraction - the core of any design 


#### 下载安装 Postgres GUI
https://www.pgadmin.org/ 
下载安装 windows/mac 客户端


#### 复习材料 (基础材料必看，进阶材料选看）
| - | 材料 | 备注 |
|---|---|---|
| 基础 | [关系型数据库入门](https://www.bilibili.com/video/av24590479?from=search&seid=9547685086593982005) | - |
| 基础 | [数据模型基础概念](https://www.guru99.com/data-modelling-conceptual-logical.html) | - |
| 基础 | [Postgresql 手册](https://www.tutorialspoint.com/postgresql/) | 可以根据需要查询关键字 |
| 基础 | [PGSQL + Python编程](https://pynative.com/python-postgresql-tutorial/) | 参考文中的例子，结合materials/python-sql-conn.ipynb |
| 进阶 | [讨论：用pgsql设计股票数据存储](https://quant.stackexchange.com/questions/29572/building-financial-data-time-series-database-from-scratch) | 只需要浏览以下即可 |
| 进阶 | [什么是时间序列数据库](https://www.bilibili.com/video/av51118320?from=search&seid=15026838482424778621) | CMU 详细介绍了 influxdb 的设计理念和time series DB |
| 进阶 | [不同环境下的docker设置](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-centos-7) | docker可以快速配置数据库等app，感兴趣的同学可以看一下 |


#### 作业
1. 数据库连接和操作
* 使用自己的名字作为用户名(如 mike)登陆数据库名为名字+db(如 mikedb)，此时密码为2019.
  example: psql -h 104.198.59.118 -U weiliu -d weiliudb 
* 使用上课讲述的数据类型(int, serial, varchar, json和timestamp)创建三个用外键关联的table
* 在每个table中插入10条数据。
* 修改table的一个column
* 删除三个table中的一个
* 将数据库SQL存在week3-data-model/homework/{$username}/create_table.sql
* （选作）给一个table中加入trigger(参考复习材料).


2. 设计数据表
* 根据课上讲解的 exchange - company - stock 关系，使用processon.com画出关系图。
* 设计python程序，将 关系图 转化为 程序设计图。
* 将两个图截图存在
week3-data-model/homework/{$username}/ER-diagram 和
week3-data-model/homework/{$username}/program-diagram


3. 简单ETL程序实现
* 根据2的设计图，转化为一个python module
* 程序需要将week3-data-model/homework/sample_data.csv转化并存储在数据库中
* 编写一个测试function, 可以验证数据存储的正确性(数量，格式等)。

