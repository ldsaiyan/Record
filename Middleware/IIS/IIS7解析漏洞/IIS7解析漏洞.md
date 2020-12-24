# IIS7解析漏洞

## 介绍
IIS7或7.5 用Fast-CGI模式下，在访问图片文件路径（如haha.jpg）后面加上/.php就会将/haha.jpg/.php解析为php文件

常常是利用上传图片木马，然后访问利用刚说的访问方式，就能执行恶意的文件。

## 版本
IIS/7.5
Windows7

## 漏洞复现
Win7安装IIS,安装php-5.2.9-2-nts-win32-installer.msi。

进入IIS，选择ISAPI或者CGI限制，添加php-cgi.exe路径

![](https://github.com/saiyanlee/Record/blob/master/Sys/IIS/IIS7解析漏洞/images/1.png)


添加脚本映射

![](https://github.com/saiyanlee/Record/blob/master/Sys/IIS/IIS7解析漏洞/images/2.png)

phpinfo测试

![](https://github.com/saiyanlee/Record/blob/master/Sys/IIS/IIS7解析漏洞/images/3.png)

制作图片木马：haha.jpg，里面内容插入了phpinfo();

![](https://github.com/saiyanlee/Record/blob/master/Sys/IIS/IIS7解析漏洞/images/4.png)

然后把文件放去访问目录下，再在本机访问该文件

![](https://github.com/saiyanlee/Record/blob/master/Sys/IIS/IIS7解析漏洞/images/5.png)

![](https://github.com/saiyanlee/Record/blob/master/Sys/IIS/IIS7解析漏洞/images/6.png)

成功执行了脚本内容;

## 防范 
在php配置文件php.ini原来的;cgi.fix_pathinfo=1改为：

![](https://github.com/saiyanlee/Record/blob/master/Sys/IIS/IIS7解析漏洞/images/7.png)