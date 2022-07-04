<style type="text/css">

    .hone {
        position: absolute;
        left: 400px;
        top: 45px;
    }

    .htwo {
        position: absolute;
        left: 505px;
        top: 43px;
    }

    .hthree {
        position: absolute;
        left: 395px;
        top: 70px;
    };
</style>

<?php
    $id = $_GET["id"];
?>

<button  ><a href="index.php">Starting Page</a></button>
<?php include "search_patient.php"?>

<br><br>

<?php
    if ($id != "None"){
        $result = exec("python3 main_logic.py $id");
        include "html_files/".$id.".html";
    }
?>