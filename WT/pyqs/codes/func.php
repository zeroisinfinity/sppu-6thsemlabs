<?php
function greet(){
    echo "Hi";
}
greet();

function add($a,$b){
    $sum = $a + $b;
    echo "Sum is " . $sum;
}
add(10,20);

function sqr($n){
    return $n * $n;
}

echo sqr(5);
?>
