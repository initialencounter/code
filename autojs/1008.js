threads.start(function () {
    var beginBtn;
        if (beginBtn = classNameContains("Button").textContains("立即开始").findOne(2000)) {
            beginBtn.click();
        }
    })
if(!requestScreenCapture()){
    toast("请求截图失败");
    exit
}
sleep(250)

function riqiang(){
    var ra = new Shell(true)
    sleep(1000)
    for(var i=0 ; i<36 ; i++){
        ra.exec('input swipe 420 775 230 890 1000')//日墙
        sleep(10000)
        ra.exec('input tap 240 430')//买装备
    }
    
}
function touxiang(){
    var ra = new Shell(true)
    sleep(1000)
    ra.exec('input tap 495 190')//设置
    sleep(1000)
    ra.exec('input tap 440 910')//投降
    sleep(10000)
    ra.exec('input tap 1200 760')//继续
    sleep(1000)
    ra.exec('input tap 2070 980')//继续
    sleep(2000)
    ra.exec('input tap 1050 900')//等下再学
    sleep(1000)
    ra.exec('input tap 2200 1000')//再玩一次
}
function manyuanjiance(){
    var ra = new Shell(true)
    sleep(1000)
    ra.exec('input tap 980 70')//大厅
    sleep(1000)
    ra.exec('input tap 1176 795')//任意位置
    res = null
    while(res==null){
        sleep(1000)
        var img1 = captureScreen()
        var num = colors.red(images.pixel(img1,1045,125))+colors.red(images.pixel(img1,1105,132))+colors.red(images.pixel(img1,1170,135))+colors.red(images.pixel(img1,1235,132))+colors.red(images.pixel(img1,1300,125))
        log(num)
        if (colors.red(images.pixel(img1,295,1020))>150){//204
            ra.exec('input tap 980 70')//大厅
        }
        if(num>1000){//1000
                res = 1
            }
        img1.recycle()
    }
    ra.exec('input tap 980 70')//大厅
    sleep(1000)
    ra.exec('input tap 2080 1000')//寻找对局
}




function duijujieshou(){
    var sh = new Shell(true)
    sleep(1000)
    res = null
    while(res==null){
        var img1 = captureScreen()
        var img = images.grayscale(img1)
        img1.recycle()
        var tm = images.read('/sdcard/脚本/rec/接受.jpg')
        var temp = images.grayscale(tm)
        tm.recycle()
        res = findImage(img, temp,{
            region: [1000, 300],
            threshold: 0.8
        });
        img.recycle()
        temp.recycle()
    }
    log(7)
    sh.exec('input tap 1200 810')//接受

    
    res = null
    while(res==null){
        sh.exec('input tap 1200 810')//接受
        var img1 = captureScreen()
        var img = images.grayscale(img1)
        img1.recycle()
        var tm = images.read('/sdcard/脚本/rec/无极剑圣.jpg')
        var temp = images.grayscale(tm)
        tm.recycle()
        res = findImage(img, temp,{
            region: [790, 200],
            threshold: 0.5
        });
        img.recycle()
        temp.recycle()
    }
    log(8)


    for(var i=1; i<6 ; i++){//选英雄
        sh.exec('input tap '+880*i+' 300')
        sleep(1000)
        sh.exec('input tap 1200 980')
    }
    log(9)
}
function kaiju(){
    res = null
    while(res==null){
        var img1 = captureScreen()
        sleep(1000)
        var num = Math.abs(colors.blue(images.pixel(img1,2180,380))-195)
        if(num<10){
            res = 1
        }
        img1.recycle()
    }
    log(0)
}
while(1){
    manyuanjiance()
    duijujieshou()
    kaiju()
    riqiang()
    touxiang()
}



// var img1 = captureScreen()
// // var num = Math.abs(colors.blue(images.pixel(img1,445,670)))
// log(colors.red(images.pixel(img1,1045,125)))
// log(colors.red(images.pixel(img1,1105,132)))
// log(colors.red(images.pixel(img1,1170,135)))
// log(colors.red(images.pixel(img1,1235,132)))
// log(colors.red(images.pixel(img1,1300,125)))
// log(colors.red(images.pixel(img1,295,1020)))
// // log(num)
// // if(num<10){
// //     log(1)
// // }
// img1.recycle()