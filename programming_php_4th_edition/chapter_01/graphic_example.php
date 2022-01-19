<?php 
if (isset($_GET['message'])) {
    
    // load font and image, calculate width of text

    $font = dirname(__FILE__) . '/fonts/Blazed.ttf';


    $size = 12;

    $image = imagecreatefrompng("button.png");

    $tsize = imagettfbbox($size, 0, $font, $_GET['message']);


    // center
    $dx = abs($tsize[2] - $tsize[0]);
    $dy = abs($tsize[5] - $tsize[3]);
    $x  = (imagesx($image) - $dx) / 2;
    $y  = (imagesy($image) - $dy) / 2 + $dy;

    // draw text 
    $black = imagecolorallocate($image, 0, 0, 0);

    imagettftext($image, $size, 0, $x, $y, $black, $font, $_GET['message']);

    // retune image

    header("Content-type: image/png");
    imagepng($image);

    exit;

}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Button Form</title>
</head>
<body>
    
    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="GET">

    Enter message to appear on button: 

    <input type="text" name="message"><br>
    <input type="submit">    
    
    </form>

</body>
</html>