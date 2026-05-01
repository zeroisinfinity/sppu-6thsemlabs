package ebookpkg;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/ebookclass")
public class ebookclass extends HttpServlet {

    private static final long serialVersionUID = 1L;

    public ebookclass() {
        super();
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // set response type
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        // start HTML
        out.println("<html>");
        out.println("<head><title>Book Data</title></head>");
        out.println("<body>");

        try {
            // database details
            String driver = "com.mysql.jdbc.Driver";
            String url = "jdbc:mysql://localhost:3306/books";
            String user = "root";
            String pass = "Sudarshan";

            // load driver
            Class.forName(driver);

            // connect to database
            Connection con = DriverManager.getConnection(url, user, pass);

            // create statement
            Statement stmt = con.createStatement();

            // query
            String sql = "SELECT * FROM ebookshop";

            // execute query
            ResultSet rs = stmt.executeQuery(sql);

            // table start
            out.println("<table border='1' style='border-collapse:collapse;'>");
            out.println("<tr>");
            out.println("<th>Book ID</th>");
            out.println("<th>Book Name</th>");
            out.println("<th>Author</th>");
            out.println("<th>Price</th>");
            out.println("<th>Quantity</th>");
            out.println("</tr>");

            int count = 0;

            // loop data
            while (rs.next()) {
                out.println("<tr>");
                out.println("<td>" + rs.getString("book_id") + "</td>");
                out.println("<td>" + rs.getString("book_name") + "</td>");
                out.println("<td>" + rs.getString("book_author") + "</td>");
                out.println("<td>" + rs.getDouble("book_price") + "</td>");
                out.println("<td>" + rs.getInt("quantity") + "</td>");
                out.println("</tr>");
                count++;
            }

            // close resources
            rs.close();
            stmt.close();
            con.close();

            // record count
            out.println("</table>");
            out.println("<p>Total records: " + count + "</p>");

        } catch (Exception e) {
            out.println("<p>Error: " + e.getMessage() + "</p>");
            e.printStackTrace();
        }

        out.println("</body></html>");
        out.close();
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // same as GET
        doGet(request, response);
    }
}
