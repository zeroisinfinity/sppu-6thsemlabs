<?php

$host = "local";
$user = "root";
$pass = "root"
$db = "mydb";

$conn = mysqli_connect($host,$user,$pass,$db);

if(!conn){
    die("fail");
}

echo "succcess"

    $sql = "INSERT INTO users (name,age) values ('Sahil',21)";
mysqli_query($conn,$sql);
mysqli_query($conn,"SELECT * FROM users");
while($row = mysqli_fetch_assoc($result)){
    echo $row['name'] . " " . $row['age']
}

mysqli_close($conn);
$corr = new PDO("mysql:host=localhost;dbname=mydb","root","");

?>

