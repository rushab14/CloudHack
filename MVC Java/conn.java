import java.sql.*;

public class conn
{
	public Connection c = null;
	public Statement stmt = null;
	
	public conn()
	{
		try
		{
			Class.forName("org.postgresql.Driver");
			c = DriverManager.getConnection("jdbc:postgresql://localhost:5432/prsystem", "postgres", "");
			stmt = c.createStatement();
		}
		catch (Exception e)
		{
			e.printStackTrace();
			System.err.println(e.getClass().getName()+": "+e.getMessage());
			System.exit(0);
		}
	}
}

