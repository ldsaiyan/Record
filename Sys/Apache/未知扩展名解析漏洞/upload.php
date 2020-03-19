<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Upload</title>
</head>
<body>
<form action="" enctype='multipart/form-data' method="post">
    <input type="file" name="filename">
    <input type="submit" name="button" value="点击上传">
</form>
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

// 判断文件类型
$fi = new finfo(FILEINFO_MIME_TYPE);
$mimeType = $fi -> file($_FILES['filename']['tmp_name']);

// 设置黑名单
$blackList = array('text/x-php','image/png');
if (in_array($mimeType,$blackList)) {
    exit("不允许上传此类型");
} else {
    // 从tmp移动到upload
    move_uploaded_file($_FILES['filename']['tmp_name'],'./upload/'.$_FILES['filename']['name']);
    echo "OK";
}

?>