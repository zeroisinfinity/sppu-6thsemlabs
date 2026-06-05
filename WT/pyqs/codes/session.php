<?php

setcookie("username","Sahil",time()+3600);
echo $_COOKIE["username"];
setcookie("username","",time-3600);

session_start();
$_SESSION["user"] = "Sahil";
echo $_SESSION["user"];
session_destroy();
?>
