# JBoss未授权访问

#### 介绍
JBoss默认配置了以下服务：
Administration Console
JMX Console
JBoss Web Services Console

默认只有Administration Console需要输入用户名和密码，默认用户名和密码都是admin。

在默认情况下， 访问 http://your-ip:8080/jmx-console 就能够进入JBoss的部署管理的信息。期间不需要输入用户名和密码，并且能够上传自己准备的木马。

在测试的时候，也连同访问web-console，看是否能进入

#### 安全配置
1、%JBOSS_HOME%/server/default/deploy/jmx-console.war/WEB-INF/jboss-web.xml 文件，开启安全配置。

去掉注释
```
<jboss-web>
<security-domain>java:/jaas/jmx-console</security-domain>
</jboss-web>
```

2、与jboss-web.xml同级目录下还有一个文件web.xml，开启安全认证。把 GET 和 POST 两行注释掉同时 security-constraint 整个部分取消注释, 不然存在head头绕过。 

3、在1中的jmx-console安全域和2中的运行角色JBossAdmin都是在%JBOSS_HOME%\server\default\conf\props\jbossws-users.properties 中配置。查找jmx-console。

```
<application-policy name=”jmx-console”>

<authentication>

<login-module code=”org.jboss.security.auth.spi.UsersRolesLoginModule”

flag=”required”>

<module-option name=”usersProperties”>props/jmx-console-users.properties</module-option>

<module-option name=”rolesProperties”>props/jmx-console-roles.properties</module-option>

</login-module>

</authentication>

</application-policy>
```
可以看到JMX Console的用户密码配置位置。


4、%JBOSS_HOME%\server\default\conf\props\jbossws-roles.properties 中定义新用户名所属角色。(格式为用户名 = 角色多个角色以 “,”)

%JBOSS_HOME%\server\default\conf\props\ jmx-console-users.properties，自行修改密码。

以上是JMX Console的安全配置

最后，如果是删除JMX Console,后重启JBoss也能解决这安全问题