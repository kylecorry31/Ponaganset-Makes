<?php 
    if(isset($_POST["command"])){
      if($_POST["command"] == "morse"){
          if(isset($_POST["text"])){
              $array = array("run" => true,
                         "command" => $_POST["command"],
                         "text" => $_POST["text"]);
              $json = json_encode($array);
              $file = fopen("commands.json", "w");
              fwrite($file, $json);
              fclose($file);
          }
      } else {
          $array = array("run" => true,
                        "command" => $_POST["command"],
                        "text" => "");
          $json = json_encode($array);
          $file = fopen("commands.json", "w");
          fwrite($file, $json);
          fclose($file);
      }
    exec("./pi.sh");
    } 
?>