// for(var i=0;i<10;i++){
threads.start(function () {
    var beginBtn;
        if (beginBtn = classNameContains("Button").textContains("立即开始").findOne(2000)){
            beginBtn.click()
        }
    })
    // if(!requestScreenCapture()){
    //     toast("请求截图失败");
    //     exit
    // }
    // sleep(1000)
    // captureScreen('/storage/emulated/0/Pictures/Screenshots/'+i+'.jpg');
    // var img = images.read('/storage/emulated/0/Pictures/Screenshots/'+i+'.jpg')
    // log(colors.toString(images.pixel(img, 1930, 50)))//点券
    // img.recycle();
    // close('/storage/emulated/0/Pictures/Screenshots/'+i+'.jpg')
// function del(x,y){
//     for(var i = x; i<y; i++){
//     files.remove('/storage/emulated/0/Pictures/Screenshots/'+i+'.png')
// }}
    

if(!requestScreenCapture()){
    toast("请求截图失败");
    exit;
}
sleep(250)
// function hs(){
// // 连续截图5张图片(间隔2秒)并保存到存储卡目录
// for(var i = 0; i < 5; i++){
//     var img = captureScreen()
    // log(colors.toString(images.pixel(img, 1930, 50)))//点券 #fffdffff
    // log(colors.toString(images.pixel(img, 1710, 50)))//钻石 #fff9f2ff
    // log(colors.toString(images.pixel(img, 660, 60)))//三角形 #ff5283b5
    // log(colors.toString(images.pixel(img, 2005, 175)))//叉叉 #ffe0e9e9
    // log(colors.toString(images.pixel(img, 1860, 90)))//比赛叉叉 #ffe1ecec
    // log(colors.toString(images.pixel(img, 2245, 912)))//小妲己 #ffe1544c
    // log(colors.toString(images.pixel(img, 850, 770)))//去领取 #ffa78654
    // log(colors.toString(images.pixel(img, 1080, 890)))//收下 #ff9d7c4a
    // log(colors.toString(images.pixel(img, 1440, 720)))//健康系统红 #ffb7234c
    // log(colors.toString(images.pixel(img, 1210, 720)))//健康系统蓝 #ff2f618a
    // log(colors.toString(images.pixel(img, 880, 725)))//爆满 #ffff3333
    // log(colors.toString(images.pixel(img, 2176, 940)))//12+ #ff1497db
    // log(colors.toString(images.pixel(img, 1750, 950)))//今日不再显示 #ff0b121d
    // log(colors.toString(images.pixel(img, 1250, 50)))//主钻石 #fff9f1ff #fff9f2ff
    // log(colors.toString(images.pixel(img, 157, 73)))//返回键 #fff0f8fe #ffeff7fe 
    // log(colors.toString(images.pixel(img, 1320, 540)))// 榜单 #fff4f4fc
    // log(colors.toString(images.pixel(img, 1275, 970)))//房主检测 #ff917047
    // log(colors.toString(images.pixel(img, 126, 1074)))//房主检测 #ff1c2840
    // log(colors.toString(images.pixel(img, 1380,980)))// 恢复 #ffbaba0d
    // log(colors.toString(images.pixel(img,1100,400 )))// 血条 #ff50c437
    // log(colors.toString(images.pixel(img, 1425,975)))// 返回房间 #ff987845 开始匹配 #ffffffff 大厅 #ff1d273e
    // log(colors.toString(images.pixel(img, 170, 205 )))// 邀请 #ffb64b42
    // log(colors.toString(images.pixel(img,500,360 )))// 
    // log(colors.toString(images.pixel(img,130,1460 )))// 错误 #fffeeced
    // log(colors.toString(images.pixel(img,130 ,1650 )))//正确 #ffebf9f1
    // log(colors.blue(images.pixel(img,144,205 )))//小狼 #ffec9d0e
    // log(colors.toString(images.pixel(img,144,205 )))//小狼 #ffec9d0e

    // log(colors.toString(images.pixel(img, )))// 
    // log(colors.toString(images.pixel(img, )))// 
    // log(colors.toString(images.pixel(img, )))// 
    // log(colors.toString(images.pixel(img, )))// 
    // log(colors.toString(images.pixel(img, )))// 
//     files.remove('/storage/emulated/0/Pictures/Screenshots/'+i+'.png')
// }}
// hs()
log(0)
captureScreen('./img.jpg')
log(1)
captureScreen("./img4.jpg")   
log(2)
var img = images.read('./img.jpg')
var img4 = images.read(('./img4.jpg'))
// log(colors.blue(images.pixel(img,144,205 )))//小狼 #ffec9d0e
// log(typeof(colors.blue(images.pixel(img,144,205 ))))
log(colors.toString(images.pixel(img,144,205 )))//小狼 #ffec9d0e
log(colors.toString(images.pixel(img4,144,205 )))//
img.recycle()
img4.recycle()