<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!--
Design by http://sc.chinaz.com
Released for free under a Creative Commons Attribution 3.0 License
-->
{% load staticfiles %}	
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>登录</title>
<script>
function check()
{

	var m=document.ss.name.value;
	var n=document.ss.password.value;
    var o=0;
    {%for user in users%}
	if (m=={{user.username}}){o=1;}
	{%endfor%}
	if (m==""){
		document.ss.explain.value="用户名不能为空!";
		document.ss.e.value="";
		document.ss.sub.type="button";
		return;
	}	
	else if (o==0){
		document.ss.explain.value="用户名不存在，请重新输入!";
		document.ss.e.value="";
		document.ss.sub.type="button";
		return;
		}
	else if (n==""){
		document.ss.explain.value="密码不能为空!";
		document.ss.sub.type="button";
		document.ss.e.value="";
		return;
	}	
	    
	else {
		document.ss.explain.value="";
		document.ss.sub.type="submit";
		document.ss.e.value="";
	}
}
</script>

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="{% static "style.css" %}" rel="stylesheet" type="text/css" />
<!-- CuFon: Enables smooth pretty custom font rendering. 100% SEO friendly. To disable, remove this section -->
<!-- CuFon ends -->
</head>
<body>
<div class="main">

   <div class="header">
    <div class="header_resize">
     <div class="logo"><h1><a href="/home/">论文<span>管理</span> <small>欢迎进入论文管理系统！</small></a></h1></div>
      <div class="menu_nav">
        <ul>
          <li><a href="/home/">主页</a></li>
          <li><a href="/reference/">参考论文</a></li>
          <li><a href="/publish/">发表论文</a></li>
          <li class="active"><a href="/login/">登录&注册</a></li>
        </ul>
      </div>
      <div class="clr"></div>
    </div>
  </div>

  <div class="content">
    <div class="content_resize">
      <div class="mainbar">
        <div class="article">
          <h2>登录您的账号</h2>
          <p>请输入您的账号和密码进行登录，如果您尚未拥有本平台的账号，请<span><a href="/register/">注册一个新的账号</a></span></p>
        </div>
        <div class="article"><div class="clr"></div>
          <form action="#" method="post" id="send" name="ss">
          <ol><li>
            {%ifequal x 1 %} <input name="e" id="e" readonly="readonly" style="border:none;" value="密码错误，请重新输入"  
            />  {%endifequal%}
            <label for="name">用户名：</label>
            <input id="name" name="name" class="text"  onblur="javascript:check()" />
          </li>
          <li>
            <label for="password">密码：</label>
            <input id="password" name="password" class="text" type="password"  onblur="javascript:check()" />
            <input name="explain" style="border:none;"  readonly="readonly">
          </li>
          <li>
             <input type="button" name="sub" value="" style="background:url('{% static "login.gif" %}')no-repeat;  width:90px; height:30px; border:none;"  />
            <div class="clr"></div>
          </li></ol>
          </form>
        </div>
      </div>
      <div class="sidebar">
        <div class="gadget">
          <h2 class="star"><span>Sidebar</span> Menu</h2><div class="clr"></div>
          <ul class="sb_menu">
            <li><a href="#">Home</a></li>
            <li><a href="#">TemplateInfo</a></li>
            <li><a href="#">Style Demo</a></li>
            <li><a href="#">Blog</a></li>
            <li><a href="#">Archives</a></li>
          </ul>
        </div>
      </div>
      <div class="clr"></div>
    </div>
  </div>

</div>
<div style="display:none"><script src='http://v7.cnzz.com/stat.php?id=155540&web_id=155540' language='JavaScript' charset='gb2312'></script></div></body>
</html>
