<%@page import="javaResources.LoginServlet"%>
<%@page import="javaResources.Dbutil"%>
<%@page import="java.sql.Statement"%>
<%@page import="com.mysql.cj.xdevapi.Table"%>
<%@page import="com.sun.prism.impl.Disposer.Record"%>
<%@page import="java.sql.Connection"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1" import="javaResources.Dbmanager"%>
<!DOCTYPE html>
<%
	
	String action = request.getParameter("action");
	String s = "";
	if(action == null){
		
	}
	else if(action.equals("login")){
		boolean logcheck = Dbutil.validateUser(request.getParameter("Username"), request.getParameter("Password"));
		if(logcheck){
			s = "success";
			request.setAttribute("user",request.getParameter("Username"));
			
		}
		else{
			s = "failed";
		}
	}

%>



<html>
<head> 
<title>web project</title>
<h1> <%=s%></h1>
  <meta charset="UTF-8">
  <link rel="stylesheet" type="text/css" href="logstyle.css">

</head>
<body>
<div class="search">
 
  <input type="text" placeholder="Search..">
</div>


<h3>Sign In</h3>





<div class="container">
  <form>
    <label for="Uname">Username</label>
    <input type="text" id="Uname" name="Username" placeholder="Username">

    <label for="Pword">Password</label>
    <input type="text" id="Pword" name="Password" placeholder="Password">

    <label for="country">University</label>
    <select id="University" name="university">
      <option value="Laurier">Wilfrid Laurier</option>
      <option value="waterloo">Waterloo</option>
      <option value="Conestoga">Conestoga College</option>
    </select>


    

    <input type="submit" value="login" name="action">
  </form>
</div>



</body>
</html>