# PUT任意文件写入

#### 前提
1、IIS6.0 （低版本）
2、可以PUT方法请求
3、WebDAV开启且配置支持多种请求（包括MOVE方法）
4、对网站有写入权限

补充：当IIS中的配置网站有写入权限的时候就可以直接PUT文件上去

#### WebDAV
WebDAV是一种基于 HTTP 1.1协议的通信协议.它扩展了HTTP 1.1，在GET、POST、HEAD等几个HTTP标准方法以外添加了一些新的方法：: PROPFIND, MOVE, COPY等。然后用这些请求，操作web服务器上的文档。

MOVE：将资源从一个URI移动到另外一个URI。

IIS实现Webdav是采用的其两种接口CGI、ISAPI的ISAPI接口。

开启WebDAV之后，IIS就支持PROPFIND、PROPPATCH、MKCOL、DELETE、PUT、COPY、MOVE、LOCK、UNLOCK等方法了。

#### 思路
有了上面的前提条件之后，就可以进行利用了。（发送OPTIONS请求，查看网站允许的请求方法，有木有PUT，MOVE等等）

先编写一个一句话木马的txt文件。再用PUT方法上传至网站。

然后再使用MOVE请求（这里利用就是把原来的txt重命名，有点像Linux的mov）把文件类型改为php、asp或者jpg等（按实际情况定）。具体的请求包如图：

![](https://github.com/saiyanlee/Record/blob/master/Sys/IIS/PUT任意文件写入/images/1.png)

图片来自网络

最后就用菜刀或者蚁剑连上去--

#### 防范
WebDAV关闭
写入权限关闭