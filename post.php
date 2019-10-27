<html>
<head>
	<title></title>
	<?php $data = json_decode(file_get_contents('php://input'), true);
	print_r($data);
	echo $data["name"]; ?>
</head>
<body>

</body>
</html>