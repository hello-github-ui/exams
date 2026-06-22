---
title: 18_SpringMVC_面试专题及答案
source: 笔试面试真题（包含面试真题和企业面试题）/面试真题-按知识点划分/18_SpringMVC_面试专题及答案.pdf
pages: 4
converted_at: 2026-06-22 22:29:21
---

# 18_SpringMVC_面试专题及答案

1、什么是SpringMvc？ 
答：SpringMvc 是spring 的一个模块，基于MVC 的一个框架，无需中间整合层来整合。 
2、Spring MVC 的优点： 
答： 
 
1）它是基于组件技术的.全部的应用对象,无论控制器和视图,还是业务对象之类的都是 java
组件.并且和Spring 提供的其他基础结构紧密集成.  
 
 2）不依赖于Servlet API(目标虽是如此,但是在实现的时候确实是依赖于Servlet 的)  
 
 3）可以任意使用各种视图技术,而不仅仅局限于JSP  
 
 4）支持各种请求资源的映射策略  
 
 5）它应是易于扩展的 
 
3、SpringMVC 工作原理？ 
答： 
 
 1）客户端发送请求到DispatcherServlet  
 
 2）DispatcherServlet 查询handlerMapping 找到处理请求的Controller  
 
 3）Controller 调用业务逻辑后，返回ModelAndView  
 
 4）DispatcherServlet 查询ModelAndView，找到指定视图  
 
 5）视图将结果返回到客户端 
 
4、SpringMVC 流程？ 
答：  
 
 1）用户发送请求至前端控制器DispatcherServlet。  
 
 2）DispatcherServlet 收到请求调用HandlerMapping 处理器映射器。 
 
 3）处理器映射器找到具体的处理器(可以根据xml 配置、注解进行查找)，生成处理器对象
及处理器拦截器(如果有则生成)一并返回给DispatcherServlet。  
 
 4）DispatcherServlet 调用HandlerAdapter 处理器适配器。  
 
 5）HandlerAdapter 经过适配调用具体的处理器(Controller，也叫后端控制器)。  
 
 6）Controller 执行完成返回ModelAndView。

---

7）HandlerAdapter 将controller 执行结果ModelAndView 返回给DispatcherServlet。  
 
 8）DispatcherServlet 将ModelAndView 传给ViewReslover 视图解析器。  
 
 9）ViewReslover 解析后返回具体View。  
 
 10）DispatcherServlet 根据View 进行渲染视图（即将模型数据填充至视图中）。  
 
 11）DispatcherServlet 响应用户。 
 
 
6、SpringMvc 的控制器是不是单例模式,如果是,有什么问题,怎么解决？ 
答：是单例模式,所以在多线程访问的时候有线程安全问题,不要用同步,会影响性能的,解决
方案是在控制器里面不能写字段。 
7、如果你也用过struts2.简单介绍下springMVC 和struts2 的区别有哪些? 
答：  
 
 1）springmvc 的入口是一个servlet 即前端控制器，而struts2 入口是一个filter 过虑器。 
 
 2）springmvc 是基于方法开发(一个url 对应一个方法)，请求参数传递到方法的形参，可以
设计为单例或多例(建议单例)，struts2 是基于类开发，传递参数是通过类的属性，只能设
计为多例。 
 
 3）Struts 采用值栈存储请求和响应的数据，通过OGNL 存取数据，springmvc 通过参数解
析器是将request 请求内容解析，并给方法形参赋值，将数据和视图封装成ModelAndView
对象，最后又将ModelAndView 中的模型数据通过reques 域传输到页面。Jsp 视图解析器默
认使用jstl。 
 
8、SpingMvc 中的控制器的注解一般用那个,有没有别的注解可以替代？ 
答：一般用@Conntroller 注解,表示是表现层,不能用用别的注解代替。 
9、 @RequestMapping 注解用在类上面有什么作用？ 
答：是一个用来处理请求地址映射的注解，可用于类或方法上。用于类上，表示类中的所
有响应请求的方法都是以该地址作为父路径。 
10、怎么样把某个请求映射到特定的方法上面？ 
答：直接在方法上面加上注解@RequestMapping,并且在这个注解里面写上要拦截的路径 
11、如果在拦截请求中,我想拦截get 方式提交的方法,怎么配置？ 
答：可以在@RequestMapping 注解里面加上method=RequestMethod.GET 
12、怎么样在方法里面得到Request,或者Session？ 
答：直接在方法的形参中声明request,SpringMvc 就自动把request 对象传入 
13、我想在拦截的方法里面得到从前台传入的参数,怎么得到？ 
答：直接在形参里面声明这个参数就可以,但必须名字和传过来的参数一样 
14、如果前台有很多个参数传入,并且这些参数都是一个对象的,那么怎么样快速得到这个对
象？

---

答：直接在方法中声明这个对象,SpringMvc 就自动会把属性赋值到这个对象里面。 
15、SpringMvc 中函数的返回值是什么？ 
答：返回值可以有很多类型,有String, ModelAndView,当一般用String 比较好。 
16、SpringMVC 怎么样设定重定向和转发的？ 
答：在返回值前面加"forward:"就可以让结果转发,譬如"forward:user.do?name=method4" 在
返回值前面加"redirect:"就可以让返回值重定向,譬如"redirect:http://www.baidu.com" 
17、SpringMvc 用什么对象从后台向前台传递数据的？ 
答：通过ModelMap 对象,可以在这个对象里面用put 方法,把对象加到里面,前台就可以通
过el 表达式拿到。 
18、SpringMvc 中有个类把视图和数据都合并的一起的,叫什么？ 
答：叫ModelAndView。 
19、怎么样把ModelMap 里面的数据放入Session 里面？ 
答：可以在类上面加上@SessionAttributes 注解,里面包含的字符串就是要放入session 里面
的key 
20、SpringMvc 怎么和AJAX 相互调用的？ 
答： 
 
通过Jackson 框架就可以把Java 里面的对象直接转化成Js 可以识别的Json 对象。  
 
 具体步骤如下 ： 
 
     1）加入Jackson.jar  
 
     2）在配置文件中配置json 的映射  
 
     3）在接受Ajax 方法里面可以直接返回Object,List 等,但方法前面要加上@ResponseBody
注解 
 
21、当一个方法向AJAX 返回特殊对象,譬如Object,List 等,需要做什么处理？ 
答：要加上@ResponseBody 注解 
22、SpringMvc 里面拦截器是怎么写的 
答：有两种写法,一种是实现接口,另外一种是继承适配器类,然后在SpringMvc 的配置文件中
配置拦截器即可：  
 
<!-- 配置SpringMvc 的拦截器 --> 
<mvc:interceptors>    
 
    
<!-- 配置一个拦截器的Bean 就可以了 默认是对所有请求都拦截 -->   
 
    
<bean id="myInterceptor" class="com.et.action.MyHandlerInterceptor"></bean>    
 
    
<!-- 只针对部分请求拦截 -->    
 
    
<mvc:interceptor>       
 
        
<mvc:mapping path="/modelMap.do" />       
 
        
<bean class="com.et.action.MyHandlerInterceptorAdapter" />   
    
</mvc:interceptor> 
</mvc:interceptors>

---

23、讲下SpringMvc 的执行流程 
答：系统启动的时候根据配置文件创建spring 的容器, 首先是发送http 请求到核心控制器
disPatherServlet，spring 容器通过映射器去寻找业务控制器，使用适配器找到相应的业务
类，在进业务类时进行数据封装，在封装前可能会涉及到类型转换，执行完业务类后使用
ModelAndView 进行视图转发，数据放在model 中，用map 传递数据进行页面显示。