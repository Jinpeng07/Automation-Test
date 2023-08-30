

## docker概述

1.什么是docker

Docker是一个开源的容器框架，基于Go语言实现，基于操作系统的虚拟化技术（有点类似于虚拟机）

Docker本身并不是容器，它是创建容器的工具，是应用容器引擎。

## docker的介绍

```
1.docker能解决虚拟机能够解决所有的问题，而且可能因为你硬件设备环境导致虚拟机没办法解决的事情
2.与虚拟机的异同点:
	相同之处:都是基于硬件平台，放在自己的操作系统中
	不同之处:虚拟机比较笨重,Docker比较轻盈
	

```



## docker的特征

```
1.Docker 分为 CE 和 EE 两大版本：

	CE 即社区版，免费，支持周期 7 个月。

	EE 即企业版，强调安全，付费使用，支持周期 24 个月
2.Docker CE 目前为止在 Linux 、Windows 10(PC) 和 macOS 上的安装。


	Docker CE 支持 64 位版本 CentOS 7，并且要求内核版本不低于 3.10。
	查看系统版本：cat /etc/redhat-release
	查看内核版本： uname -r

```



## docker的环境

```
1.在云服务器上面部署docker
2.利用docker提供的容器技术封装lamp环境
3.lamp环境中，部署web页面（表单html页面）

finalshell ---->用来连接云服务器上面的操作系统centos7.5
winscp---->实现物理机系统与云服务器系统的交互工作
```



## docker的安装

```
安装docker
# yum install -y docker
查看docker的版本
# docker version
# systemctl start docker //启动 
# systemctl enable docker //添加入开机启动
```



## 云服务器配置

看购买云服务器文档

## docker的配置

```
搭建LAMP环境的主要方案分别是： 
1. 一个镜像直接包含全部（简单才是最好用的） 
2. apache、mysql、php独立连接。

搜索被收藏或使用较多的LAMP镜像，小伙伴们都推荐使用tutum/lamp
# docker search -s 10 lamp 

# docker pull docker.io/tutum/lamp //下载LAMP镜像 
# docker images//查看镜像

创建LAMP容器
# mkdir /mysql_data 
# docker run -d --name=lamp -p 8080:80 -p 3306:3306 -v /mysql_data:/var/lib/mysql docker.io/tutum/lamp

进入容器
# docker exec -it lamp /bin/bash
# mysql_secure_installation  //初始化数据库
mysql_secure_installation
按下回城键你会看见结尾如下的对话。 
Enter current password for root (enter for none):<–初次运行直接回车 
Set root password? [Y/n] <– 是否设置root用户密码，输入y并回车或直接回车 
New password: <– 设置root用户的密码 
Re-enter new password: <– 再输入一次你设置的密码 
Remove anonymous uclear
sers? [Y/n] <– 是否删除匿名用户，回车 
Disallow root login remotely? [Y/n] <–是否禁止root远程登录,回车 
Remove test database and access to it? [Y/n] <– 是否删除test数据库，回车 
Reload privilege tables now? [Y/n] <– 是否重新加载权限表，回车

All done! If you’ve completed all of the above steps, your MariaDB 
installation should now be secure.

Thanks for using MariaDB!

进入mysql
mysql -uroot -p"自己的数据库密码" 
create database wp; #创建数据库
\q 退出mysql
```



## LAMP项目部署

```
页面模板导入
apt update
cd /var/www/html
打开winscp，连接云服务器，
把biaodan.html文件拖入到var目录中，
然后执行下列命令
docker cp /var/biaodan.html  lamp:/var/www/html/

开放云服务器80和8080的端口
看文档
```



