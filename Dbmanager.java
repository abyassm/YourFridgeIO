package javaResources;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Dbmanager {

	public Connection getConnection() {
		try {

			Class.forName("com.mysql.jdbc.Driver");
			Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/db","root","root");
			return conn;
		}
		catch(ClassNotFoundException e) {
			return null;
		} catch(SQLException e) {
			return null;
		}
	}	
	
	/*
	 String query = "SELECT * FROM users";

     // create the java statement
     Statement st = conn.createStatement();
     
     // execute the query, and get a java resultset
     ResultSet rs = st.executeQuery(query);
     
     // iterate through the java resultset
     while (rs.next())
     {
       int id = rs.getInt("id");
       String firstName = rs.getString("first_name");
       String lastName = rs.getString("last_name");
       Date dateCreated = rs.getDate("date_created");
       boolean isAdmin = rs.getBoolean("is_admin");
       int numPoints = rs.getInt("num_points");
       
       // print the results
       System.out.format("%s, %s, %s, %s, %s, %s\n", id, firstName, lastName, dateCreated, isAdmin, numPoints);
     }
     st.close();

	*/
	
	

}
