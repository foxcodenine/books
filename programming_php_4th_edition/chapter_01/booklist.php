<!-- 
// Package vlucas/phpdotenv
// https://github.com/vlucas/phpdotenv

to install:     $ composer require vlucas/phpdotenv
 -->

<?php
// _____________________________________________________________________
//  loading all packages from vendor/autoload;

    $vender_autoload_path  = __DIR__ . '/vendor/autoload.php';
    require_once($vender_autoload_path);
?>


<?php
// _____________________________________________________________________
// loading .env variables;
    $env_path = realpath(__DIR__);

    $dotenv = Dotenv\Dotenv::createImmutable($env_path);
    $dotenv->load();

    

?>

<?php

$db = new mysqli($_ENV['DB_HOST'], $_ENV['DB_NAME'], $_ENV['DB_PASSWORD'], $_ENV['DB_NAME']);

if ($db->connect_errno) {
    die("Connecting Error ({$db->connect_errno}) {$db->connect_errno}"); 
}

$sql = "SELECT * FROM pp4_books WHERE available = 1 ORDER BY title";

$result = $db->query($sql);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Booklist</title>
</head>
<body>
    
    <table cellSpacing="2" cellPadding="6" align="center" border="1">

        <tr>
        <td colspan="4">
        <h3 align="center">These Books are currently available</h3>
        </td>
        </tr>

        <tr>
        <td align="center">Title</td>
        <td align="center">Year Published</td>
        <td align="center">ISBN</td>

        <tr>

        <?php while ($row = $result->fetch_assoc()) {?>

            <tr>
            <td><?php echo stripslashes($row['title']); ?></td>
            <td align="center" ><?php echo $row['pub_year']; ?></td>
            <td><?php echo $row['ISBN']; ?></td>
            </tr>

        <?php }?>
        </tr>

        </tr>
    </table>
</body>
</html>