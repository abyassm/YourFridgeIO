package javaResources;

import java.sql.*;

import com.sun.prism.impl.Disposer.Record;




public class Dbutil {
	public static void insertInDb(String statement) throws SQLException {
		
		Dbmanager Dbm = new Dbmanager();
		Connection c =  Dbm.getConnection();
		Statement st = c.createStatement();
		
		//example statement
		//"INSERT INTO table1 (string123 ,idtest) VALUES ('test', 200)"
		st.execute(statement);
		c.close();
		
	}
	public static ResultSet getFromDb(String statement) throws SQLException {
		Dbmanager Dbm = new Dbmanager();
		Connection c =  Dbm.getConnection();
		
		//SELECT * FROM recipesTable WHERE rName=
		Statement st = c.createStatement();
		ResultSet rs = st.executeQuery(statement);
		c.close();
		return rs;
	}
	public static boolean validateUser(String username,String password) throws SQLException {
		Dbmanager Dbm = new Dbmanager();
		Connection c =  Dbm.getConnection();
		
		//SELECT * FROM userTable WHERE username=? and password=?"
		Statement st = c.createStatement();
		String statement = "SELECT * FROM usertable WHERE username='"+username+"' AND password='"+password+"'";
		ResultSet rs = st.executeQuery(statement);
		boolean flag;
		flag = rs.next();
		return flag;
	}
}
