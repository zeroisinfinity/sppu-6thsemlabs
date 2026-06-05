<?php

$conn = new mysqli("localhost","root","","mydb");

if($conn -> connect_error){
}


$sql = "INSERT INTO students(name, age)
VALUES('Sahil',21)";

if($conn -> query($sql) === TRUE){
}


?>
