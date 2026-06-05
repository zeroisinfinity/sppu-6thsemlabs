public class LoginAction extends ActionSupport{
    public String execute(){
        return SUCCESS;
    }
}

<action name="login" class="LoginAction">
<result name="success">welcome.jsp</result>
</action>
