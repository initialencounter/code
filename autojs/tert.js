
function reqres(){
threads.start(function () {
    sleep(1000)//反悔时间
    var beginBtn;
        if (beginBtn = classNameContains("Button").textContains("立即开始").findOne(2000)) {
            beginBtn.click();
        }
    })
if(!requestScreenCapture()){
    toast("请求截图失败");
    exit
}
}
function capsrn(){
sleep(1000)
captureScreen('/storage/emulated/0/Pictures/Screenshots/0.png')
}
function col(x,y){
    var img = images.read('/storage/emulated/0/Pictures/Screenshots/0.png');
    var msg = colors.toString(images.pixel(img, x, y));
    log(msg)
    img.recycle()
    return msg
}
function login(){
    if (col(880, 725) == '#ffff3333'){
        if(col(2176, 940) == '#ff1497db'){
            click(1150,850)
            toast('登录')
        }
        
    }
}
function cls(){
    while(col (2005, 175)=='#ffe0e9e9'){//关闭弹窗
        click(2005,175)
        toast('关闭弹窗')
        capsrn()
        col (2005, 175)
    }
    sleep(5000)
    capsrn()
    if (col(1860, 90)=='#ffe1ecec'){
        click(1860,90)
        toast(('关闭弹窗'))
    }
    
}
function take(){
    capsrn()
    if(col(2245, 912)=='#ffe1544c'){//领取奖励
        click(2245,912)
    }
}

function local(){
capsrn()
if(col(1930, 50)=='#fffeffff'){
    if(col(1710, 50)=='#fffbf3ff'){
        if(col( 660, 60)=='#ff5182b4'){
            log('站令')
        }else{
            if(col(660, 60)=='#ff273854'){
                log('背包')
            }else{
                log('商店')
            }
        }


    }else{
        log('定制')
    }
}
capsrn()
if(col (1700, 50)=='#ff090e15'){
    log('组队')
}
capsrn
if(col( 1469, 49)=='#fcfefe'){
    log('主界面')
}
}
reqres()
capsrn()
// login()
// sleep(10000)
// capsrn()
// sleep(1000)
// cls()

// log(col( 1930, 50))//点券
// files.remove('/storage/emulated/0/Pictures/Screenshots/0.png')