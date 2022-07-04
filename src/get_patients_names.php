<?php
    //echo "<option value=\"None\"></option>";
    //echo "<a>None</a>";
    
    if ($handle = opendir('./data')) {
        $count = 1;
        
        while (false !== ($entry = readdir($handle))) {
    
            if ($entry != "." && $entry != "..") {
                $entry = substr($entry, 0, -5);
                //echo "<option value=".$entry.">".$entry."</option>";
                echo "<a href=patients.php?id=$entry>$entry</a>";
            }
            $count+=1;
        }
    
        closedir($handle);
    }
?>