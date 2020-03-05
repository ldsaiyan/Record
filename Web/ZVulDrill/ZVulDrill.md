## 介绍
ZVulDrill是一个简单并且组合了多种Web漏洞于一身的Web漏洞演练平台，非常基础

- SQL注入获取数据库信息
- SQL注入绕过管理后台登陆
- 反射型XSS
- 储存型XSS
- CSRF
- 文件上传
- 暴力破解
- 权限跨越
- 文件包含

## 开工
#### SQL注入
进去网站，映入眼帘的就是这个搜索框，拿起检测一下
![](https://github.com/saiyanlee/Record/blob/master/Web/ZVulDrill/images/1.png)
![](https://github.com/saiyanlee/Record/blob/master/Web/ZVulDrill/images/2.png)

存在注入点，然后写个sqli.py脚本，解决战斗。

然后进入后台登录入口，来个普通的万能密码，密码随便输
![](https://github.com/saiyanlee/Record/blob/master/Web/ZVulDrill/images/3.png)
![](https://github.com/saiyanlee/Record/blob/master/Web/ZVulDrill/images/4.png)

成功绕过

#### XSS
逛了一下，发现用户名这里很可疑，编辑可以提交修改用户名的表单
![](https://github.com/saiyanlee/Record/blob/master/Web/ZVulDrill/images/5.png)

操作一番，它出现了
![](https://github.com/saiyanlee/Record/blob/master/Web/ZVulDrill/images/6.png)
![](https://github.com/saiyanlee/Record/blob/master/Web/ZVulDrill/images/7.png)

回到搜索框这里，看看反射型XSS存不存在
![](https://github.com/saiyanlee/Record/blob/master/Web/ZVulDrill/images/8.png)

OK

随后，想到留言板这里试了下，失败了，估计是输入被净化了
![](https://github.com/saiyanlee/Record/blob/master/Web/ZVulDrill/images/9.png)

#### CSRF
修改密码，bp捉包转去CSRF PoC generator，然后进行验证，原密码为321，改为123作为试验
![](https://github.com/saiyanlee/Record/blob/master/Web/ZVulDrill/images/10.png)
![](https://github.com/saiyanlee/Record/blob/master/Web/ZVulDrill/images/11.png)

submit后密码就被成功改为了123，说明存在CSRF

#### 文件上传
来到改头像这里，准备了个一句话木马php文件，打算先直接上传php文件试下，没想到网站原来连内裤都没穿，直接就进去了
![](https://github.com/saiyanlee/Record/blob/master/Web/ZVulDrill/images/12.png)

头像应该是放在images文件夹上的，直接蚁剑连接
![](https://github.com/saiyanlee/Record/blob/master/Web/ZVulDrill/images/13.png)

#### 权限跨越
