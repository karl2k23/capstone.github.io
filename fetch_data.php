<?php
$servername = "sql12.freesqldatabase.com";
$dbname = "sql12672580";
$username = "sql12672580";
$password = "KetWXbpE2z";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT ID, RECORDED_DATA, WATERLEVEL, TEMPERATURE, HUMIDITY FROM ESPDATA";
$result = $conn->query($sql);

$data = array();

if ($result->num_rows > 0) {
    // Output data of each row
    while($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
} else {
    $data[] = array("message" => "No results found");
}

$conn->close();

header('Content-Type: application/json');
echo json_encode($data);
?>
