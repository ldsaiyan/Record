# Weblogic 弱口令&后台getshell

## 介绍
访问 http://192.168.140.137:7001/console 
会跳到 http://192.168.140.137:7001/console/login/LoginForm.jsp页面

![](https://github.com/saiyanlee/Record/blob/master/Sys/Weblogic/Weblogic%20%E5%BC%B1%E5%8F%A3%E4%BB%A4%26%E5%90%8E%E5%8F%B0getshell/images/1.png)


弱口令登录（参考https://cirt.net/passwords?criteria=WebLogic，或者字典爆破）

![](https://github.com/saiyanlee/Record/blob/master/Sys/Weblogic/Weblogic%20%E5%BC%B1%E5%8F%A3%E4%BB%A4%26%E5%90%8E%E5%8F%B0getshell/images/2.png)

点击左侧的部署，接着安装

![](https://github.com/saiyanlee/Record/blob/master/Sys/Weblogic/Weblogic%20%E5%BC%B1%E5%8F%A3%E4%BB%A4%26%E5%90%8E%E5%8F%B0getshell/images/3.png)

上传文件，选择要部署的war包

![](https://github.com/saiyanlee/Record/blob/master/Sys/Weblogic/Weblogic%20%E5%BC%B1%E5%8F%A3%E4%BB%A4%26%E5%90%8E%E5%8F%B0getshell/images/4.png)

![](https://github.com/saiyanlee/Record/blob/master/Sys/Weblogic/Weblogic%20%E5%BC%B1%E5%8F%A3%E4%BB%A4%26%E5%90%8E%E5%8F%B0getshell/images/5.png)

下一步，再下一步，点击完成即可。

状态处于活动，未启动的话就手动启动

![](https://github.com/saiyanlee/Record/blob/master/Sys/Weblogic/Weblogic%20%E5%BC%B1%E5%8F%A3%E4%BB%A4%26%E5%90%8E%E5%8F%B0getshell/images/6.png)

访问：http://your-ip:port/[war包名]/[包名内文件名]
就行


所以，这样就可以来上传war木马getshell