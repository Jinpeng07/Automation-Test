## jenkins的介绍

```
jenkins是什么?
Jenkins是一个开源的、提供友好操作界面的持续集成(CI)工具
CI/CD是什么？
 CI(Continuous integration，中文意思是持续集成)是一种软件开发时间。持续集成强调开发人员提交了新代码之后，立刻进行构建、（单元）测试。根据测试结果，我们可以确定新代码和原有代码能否正确地集成在一起。
 CD(Continuous Delivery， 中文意思持续交付)是在持续集成的基础上，将集成后的代码部署到更贴近真实运行环境(类生产环境)中。

 他可以做什么?
 可以定时的执行python测试脚本,
 如,原来有3个模块,然后规定2023年10月1日,必须集成A模块进入到原来3个模块中,我们要进行测试,这时候我们可以先写好测试脚本,然后在2023年10月1日准时执行这个测试脚本,那么我们的jenkins就可以做到
可以定时执行接口测试(定时执行接口自动化测试脚本)
```

## jenkins的安装

```
docker下安装jenkins
1.启动docker,下载镜像(如果你是root用户就不需要写sudo)
sudo docker pull jenkins:2.60.3
2.查看下载的镜像
docker images
3.服务器的宿主机上创建一个目录(/home/jenkins_maker),并赋予这个目录777权限
mkdir  /home/jenkins_maker
chmod 777 /home/jenkins_maker
4.创建并启动jenkins
docker run -d -p 9200:8080 -p 9201:50000 -v /home/jenkins_maker:/var/jenkins_maker -v /etc/localtime:/etc/localtime --name jenkins_ht jenkins/jenkins:2.60.3
参数说明:
-d:后台运行镜像
-p 9200:8080 将镜像的8080端口映射到服务器的9200端口
-p 9201:50000 将镜像的50000端口映射到服务器的9201端口
-v /home/jenkins_maker:/var/jenkins_maker 工作目录为/var/jenkins_maker,然后把这个目录映射到服务器的/home/jenkins_maker
-v /etc/localtime:/etc/localtime 同步容器时间和服务器一样
--name jenkins_ht 给容器取别名
jenkins/jenkins:2.60.3 要启动的镜像
5.开通阿里云服务器上的9200和9201端口
6.打开浏览器输入:ip地址:9200,就可以打开jenkins的设置界面
7.获取初识密码,页面上有提示在哪个目录下的哪个文件,提示如下:
/var/jenkins_home/secrets/initialAdminPassword
但是,我们是把docker中的jenkins工作目录挂载到了我们宿主机上,所以上面的地址应该为:
/home/jenkins_maker/secrets/initialAdminPassword
查看密码:cat /home/jenkins_maker/secrets/initialAdminPassword
然后把密码输入到页面的输入框
243a6a0e46cc414f93fbbafe982d4875
如果没有挂载成功,也可以进入docker查看:
docker exec -it jenkins_ht bash
cat /var/jenkins_home/secrets/initialAdminPassword


下载地址:https://mirrors.tuna.tsinghua.edu.cn/jenkins/windows/2.300/
注意要有jdk
看文档安装
```

## 项目自动化测试-jenkins持续集成

```
1.使用jenkings部署自动化脚本
看文档操作
```