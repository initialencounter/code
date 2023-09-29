// requestScreenCapture();
// launchApp("QQ");
// sleep(1200);
// var p = findColorEquals(captureScreen(), "#f64d30");
// if(p){
//     toast("有未读消息");
// }else{
//     toast("没有未读消息");
// }
requestScreenCapture(true);
//截图
var img = captureScreen();
//获取在点(100, 100)的颜色值
var color = images.pixel(img, 1300, 640);
//显示该颜色值
log(color)
if(color=='-14541823'){
    log(123)
}
// var img = images.read("/sdcard/1.png");
// //判断图片是否加载成功
// if(!img){
//     toast("没有该图片");
//     exit();
// }
//在该图片中找色，指定找色区域为在位置(400, 500)的宽为300长为200的区域，指定找色临界值为4
// var point = findColor(captureScreen(), "#E8C543", {
//      region: [1300, 640, 5, 5],
//      threshold: 4
//  });
// if(point){
//     toast("找到啦:" + point);
// }else{
//     toast("没找到");
// }
// var file = document.querySelector("p1.jpg").file[0]
// var img = images.read('/p1.jpg')
// var color = images.pixel(img, 1300, 640)
// // //显示该颜色值
// log(color)
