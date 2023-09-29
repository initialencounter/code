// app.startActivity({
//     action : 'VIEW',
//     packageName : 'com.duowan.kiwi',
//     className : 'com.duowan.kiwi.homepage.Homepage'
// })
// id('search_ll').click()
// id('search_content').findOne().setText('31520')
// id('search_btn').findOne().click()
// "ui";
// //ui布局为一块画布
// ui.layout(
//     <vertical>
//         <canvas id="board"
//         h = "*"
//          w = "*"/>
//     </vertical>
// );



// ui.board.on("draw", function(canvas) {  
//   var paint = new Paint();
//  //设置画笔为填充，则绘制出来的图形都是实心的
//   paint.setStyle(Paint.Style.FILL);
//  //设置画笔颜色为红色
//   paint.setColor(colors.parseColor("#ffc0cb"));
//   //绘制一个从坐标(0, 0)到坐标(500, 500)的正方形
//   canvas.drawRect(0, 0, 500, 500, paint);
// }) 
// var bol = true
// while(bol){
// var a = className("android.view.View").text('虎牙北慕慕慕').findOne().bounds().centerY()
// if(a>500 & a<2000){
//     bol = false
// }else{
//     var a = className("android.view.View").text('虎牙北慕慕慕').findOne().bounds().centerY()
//     if(a<1200){
//         swipe(555,1000,555,1450,200)
//     }else if(a>1200){
//         swipe(555,1450,555,1000,200)
//     }
// }
// }
// var arr = []
// var arrr = []
// className("android.widget.FrameLayout").clickable(true).depth(1).findOne().children().forEach(child => {
//     target  =child.findOne((clickable(true)))
//     arr.push(target)
// })
// arr[2].children().forEach(child => {
//     target  =child.findOne((clickable(true)))
//     arrr.push(target)})
// arrr[13].click()
// click()
// function shift_lists(){//切换苹果QQ区
//     var shift_list = className("android.view.View").text('手Q苹果区').findOne().bounds()
//     sleep(200)
//     click(shift_list.centerX(),shift_list.centerY())
//     sleep(100)
//     className("android.view.View").text("确定").findOne().click()
// }  
// shift_lists()
// className("android.view.View").scrollable(true).depth(5).findOne().scrollForward()
// var a = className("android.view.View").text('虎牙北慕慕慕').findOne().bounds()
// var b = className("android.view.View").scrollable(true).depth(5).findOne().bounds()
// log(a.top,b.top,a.bottom,b.bottom)
// if(a.top>b.top&a.bottom<b.bottom){
//     log(123)
// }
// function freetime(){
//     var i=0
//     while(i<5){
//         log(i)
//         var scrc_state = !device.isScreenOn()
//         sleep(1000)
//         if(scrc_state){
//             i++
//         }else{
//             i=0
//         }
//     }
//     device.wakeUp()
//     swipe(555, 1000, 600, 500, 200)

// }
// freetime()1

// function closeapp(packageName) {
//     var name = packageName; 
// if(!name){
//     if(getAppName(packageName)){
//         name = packageName;
//     }else{
//         return false;
//     } 
// }
// toastLog('打开设置'+app.getAppName(name)+'应用页面')
// app.openAppSetting(name);
// text(app.getAppName(name)).waitFor();  
// let is_sure = textMatches(/(.*强.*|.*停.*|.*结.*|.*行.*)/).findOne();
// if (is_sure.enabled()) {
//         sleep(1000)
//         textMatches(/(.*强.*|.*停.*|.*结.*|.*行.*)/).findOne().click();
//         sleep(1000)
//         id("button1").findOne().click()
//         toastLog(app.getAppName(name) + "应用已被关闭");
//         sleep(1000);
//         back();
//         sleep(1000)
//     } else {
//         log(app.getAppName(name) + "应用不能被正常关闭或不在后台运行");
//         back();
//     }
// }
// closeapp('com.wisedu.cpdaily')
// threads.start(function () {
//     var beginBtn;
//     if (beginBtn = classNameContains("Button").textContains("立即开始").findOne(2000)) {
//         beginBtn.click();
//     }
// })
// if (app.launchPackage("com.ss.android.ugc.aweme")) {
//     toastLog("抖音打开成功！");
//     if (!requestScreenCapture(false)) {
//         toastLog("请求截图失败");
//         exit();
//     }
// }
// threads.start(function () {
//     var beginBtn;
//         if (beginBtn = classNameContains("Button").textContains("立即开始").findOne(2000)) {
//             beginBtn.click();
//         }
//     })

// if (!requestScreenCapture()) {
//     toast("请求截图失败");
//     exit
// }
// var date = new Date()
// var img = captureScreen()
// var data_str = date.toString()
// var reg = new RegExp(' ', 'g')
// var name_ = data_str.replace(reg, '').slice(3, 20)+'.jpg'
// var yanzhi = 7112
// function Face_recognition(img) {
//     var ak = '8kawU4KnlvCMIZNW7wgi7rvp';//你的人脸识别ak
//     var sk = 'DdSCPGAe3100DybVWoq1BbdPsvrFLIic';//你的人脸识别sk
//     var access_token = http.get("https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + ak + "&client_secret=" + sk).body.json().access_token;
//     var url = "https://aip.baidubce.com/rest/2.0/face/v3/detect" + "?access_token=" + access_token;
//     var image64 = images.toBase64(img);
//     if (img) {
//         var res = http.post(url, {
//             headers: {
//                 'Content-Type': 'application/json; charset=UTF-8'
//             },
//             'image': image64,
//             'image_type': 'BASE64',
//             'face_field': 'beauty'
//         });
//         var str = JSON.parse(res.body.string());
//         if (str['error_msg'] == 'pic not has face') {
//             log(countVid + ".没有检测到人脸！");
//             toast("没有检测到人脸！");
//         } else if (str['error_msg'] == 'SUCCESS') {
//             yanzhi = str['result']['face_list'][0]['beauty']
//             toastLog(yanzhi)
//         }
//     }
// }
// Face_recognition(img)
// images.save(img, './img/' + name_)
// img.recycle()
// var conten = "'"+name_+"' : "+yanzhi+",\n"
// files.append('./yanzhi.txt',conten)
// events.setKeyInterceptionEnabled('volume_up',true )
// events.observeKey();
// events.onKeyDown('volume_up', ()=>{
//     log(112)
// })
// //启用按键监听
// events.observeKey();
// //监听音量下键弹起
// events.onKeyDown("volume_down", function(event){
//     toast("音量上键弹起");
// });
// //监听Home键弹起
// events.onKeyDown("home", function(event){
//     toast("Home键弹起");
//     exit();
// });
// var sh = new Shell(true)
// sleep(500)
// sh.exec('input tap 500 1100')
// sleep(100)
// sh.exec('input tap 500 1100')
// sleep(500)
// sh.exit()
function initIfNeeded() {
    runtime.images.initOpenCvIfNeeded();
}

var Range = org.opencv.core.Range;
var Core = org.opencv.core.Core;
var Imgcodecs = org.opencv.imgcodecs.Imgcodecs;
var Mat = org.opencv.core.Mat;
var MatOfPoint = org.opencv.core.MatOfPoint;
var MatOfPoint2f = org.opencv.core.MatOfPoint2f;
var Point = org.opencv.core.Point;
var Core = org.opencv.core.Core;
var vector = java.util.Vector;
var Imgproc = org.opencv.imgproc.Imgproc;
var Utils = org.opencv.android.Utils;
var CvType = org.opencv.core.CvType;
var Scalar = org.opencv.core.Scalar;
var Size = org.opencv.core.Size;
var Rect = org.opencv.core.Rect;
var ArrayList = java.util.ArrayList;

function fileIsExists(fileStr) {
    if (!files.exists(fileStr) || files.isDir(fileStr)) throw new Error("文件不存在或为文件夹");
}

function saveImage(imgFile, mat) {
    if (!java.lang.Class.forName("org.opencv.core.Mat", true, context.getClass().getClassLoader()).isInstance(mat)) throw new Error("参数类型不对");
    files.createWithDirs(imgFile);
    fileIsExists(imgFile);
    return Imgcodecs.imwrite(files.path(imgFile), mat)
}

function readImage() {
    var flags = 1;
    fileIsExists(arguments[0]);
    if (arguments.length == 2) {
        if (typeof flags != "number") throw new Error("参数类型错误");
        flags = arguments[1]
    }
    return Imgcodecs.imread(files.path(arguments[0]), flags);
}

var bg = readImage("./img/Sep19202123:55:35.jpg");
var range1 = new Range(0, 0);
var range2 = new Range(100, 100);
var roi = new Mat(bg, range1, range2);
log(bg,range1,range2,roi)