<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Upload</title>
</head>
<body>
<form action="" enctype='multipart/form-data' method="post" >
    <input type="file" name="filename" id="filename" >
    <input type="text" name="name" id="text">
    <input type="submit" name="button" value="点击上传" onmousemove="return checksubmit()">
</form>
<script>
    function checksubmit () {
        var name = document.getElementById("filename");
        var filename = name.value;
        document.getElementById("text").value = filename;
    }

</script>
</body>
</html>
<?php
// 请求失败
if (empty($_POST)) {
    exit();
}

// 上传失败
if ($_FILES['filename']['error'] != 0) {
    exit("上传失败");
}

// 获取文件名
$name = basename($_POST['name']);
print_r($name);

// 设置黑名单
$blackList = array('php','phtml','pht','php3','php4','php5');
$ext = pathinfo($name,PATHINFO_EXTENSION);
if (in_array($ext,$blackList)) {
    exit("不支持此文件");
} else {
    // 从tmp移动到upload
    move_uploaded_file($_FILES['filename']['tmp_name'],'./'.$name);
    echo "OK";
}

?>