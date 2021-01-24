<?php

$db = new mysqli("localhost", "admin", "umbrella", "library");

if ($db->connect_errno) {
    die("Connecting Error ({$db->connect_errno}) {$db->connect_errno}"); 
}

$sql = "SELECT * FROM books WHERE available = 1 ORDER BY title";

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