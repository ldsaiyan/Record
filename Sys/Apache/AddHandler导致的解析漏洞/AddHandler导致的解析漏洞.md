# AddHandler导致的解析漏洞

其实就是配置不当造成的。

最核心就在
```
AddHandler application/x-httpd-php .php
```

这个AddHandler就是把PHP文件送到php模块（三种php与Apache结合方式的其中一种）去解析了。只要文件名中含有.php后缀，就会被识别成PHP文件。

index.php.jpeg这种命名也不例外，会被当作php文件解析。解析漏洞因此产生。

![](https://github.com/saiyanlee/Record/blob/master/Sys/Apache/AddHandler导致的解析漏洞/images/1.png)


可以利用其解析漏洞绕过白名单限制。