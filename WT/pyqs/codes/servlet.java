import java.io.*;
import java.servlet*;
import java.servlet.http.*;

public class DemoServlet extends HttpServlet{
    public void init(){
    }

    public void service(HttpServletRequest req , HttpServletRespons res) 
    throws IOexception{
    res.getWriter().println();
    }
    
    public void destroy(){};
}
