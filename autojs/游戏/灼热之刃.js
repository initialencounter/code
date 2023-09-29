
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

function lunch(){//启动
    launchApp('王者荣耀');
    sleep(10000);
}
function login(){//登录
    captureScreen('./img.jpg')
    var img = images.read('./img.jpg')
    while(Math.abs(colors.red(images.pixel(img, 880, 725)))-255<10 ){
        img = captureScreen()
        log(1)
    }    
    click(1150,850)
    toast('登录')
    img.recycle()
    sleep(10000)
}
function close(){//关闭弹窗
    captureScreen('./img.jpg')
    var img = images.read('./img.jpg')
    while((colors.toString(images.pixel(img, 1250, 50))) != '#fff9f2ff'){
        if(colors.toString(images.pixel(img, 157, 73)) == '#ffeff7fe'){//返回
            click(157, 73)
            toast('返回')
        }if(colors.toString(images.pixel(img, 157, 73)) == '#ffd9e1ea'){//组队返回
            click(157, 73)
            toast('返回')
        }else if(colors.toString(images.pixel(img, 1440, 720)) == '#ffb7234c'){//健康系统
            click(1440, 720)
            toast('返回')
        }else if(colors.toString(images.pixel(img, 157, 73)) == '#ffe6f2fd'){//社区
            click(157, 73)
            toast('返回')
        }else if(colors.toString(images.pixel(img, 1320, 540)) == '#fff4f4fc'){//榜单
            click(1320, 540)
            toast('关闭榜单')
        }else if(colors.toString(images.pixel(img, 157, 73)) == '#ff1e2f45'){//赛事
            click(157, 73)
            toast('返回')
        }else if(colors.toString(images.pixel(img, 157, 73)) == '#fff0f8fe'){//小妲己
            click(157, 73)
            toast('返回')
        }else if(colors.toString(images.pixel(img, 2005, 175))=='#ffe0e9e9'){//弹窗
            click(2005,175)
            toast('关闭弹窗')
        }else if(colors.toString(images.pixel(img,1860, 90))=='#ffe1ecec'){//比赛直播
            click(1860,90)
            toast(('关闭弹窗'))
        }
        sleep(2000)
        captureScreen('./img.jpg')
        var img = images.read('./img.jpg')
    }
    img.recycle()
}

function takethings(){//领取奖励
    sleep(2000)
    images.save(captureScreen(),'./img.jpg','jpg',100)
    var img = images.read('./img.jpg')
    if(colors.toString(images.pixel(img,2245, 912))=='#ffe1544c'){//领取奖励
        click(2245,912)
        sleep(2000)
        img = captureScreen()
        if(colors.toString(images.pixel(img, 850, 770)) =='#ffa78654'){
            click(850,770)
            sleep(2000)
            img = captureScreen()
            if(colors.toString(images.pixel(img, 1080, 890)) == '#ff9d7c4a'){
                click(1080,890)
                sleep(2000)
                click(1180,860)//确定
                sleep(2000)
                click(200,50)//返回
            }
        }
    }
}
function teamsite(){//开5v5房间
    // cls()
    sleep(2000)
    click(1000,800)
    sleep(500)
    click(500,550)
    sleep(500)
    click(500,550)
}
function hhcheck(){//房主检测
    images.save(captureScreen(),'./img.jpg','jpg',100)
    var img = images.read('./img.jpg')
    if (colors.toString(images.pixel(img, 126, 1074)) == '#ff1c2840'){
        return 1
    }
}
function teamcheck(img){//检测是否满员
    images.save(captureScreen(),'./img.jpg','jpg',100)
    var img = images.read('./img.jpg')
    img = img || captureScreen();
    var x = 382;
    var n = 0;
    while(x<1455){
        images.save(captureScreen(),'./img.jpg','jpg',100)
        var img = images.read('./img.jpg')
        if(colors.toString(images.pixel(img, x, 515)) == '#ff233a5b'){
            if(colors.toString(images.pixel(img, x, 420)) == '#ff1f2f47'){
                n++;
            }
        }
        x+=268;
    }
    img.recycle()
    return n
}
function Baidu_OCR(img) {//调用API
    access_token = http.get("https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=YIKKfQbdpYRRYtqqTPnZ5bCE&client_secret=hBxFiPhOCn6G9GH0sHoL0kTwfrCtndDj").body.json().access_token;
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic" + "?access_token=" + access_token;
    imag64 = images.toBase64(img,'jpg',50);
    res = http.post(url, {headers: {'Content-Type': 'application/x-www-form-urlencoded'},image: imag64,image_type: "BASE64",language_type:"JAP"});
    str = JSON.parse(res.body.string()).words_result.map(val => val.words).join('\n');
    return str;
}
function sentmsg(){
    for(var i=1; i<6; i++){
        var nam1;
        var nam2;
        var nam3;
        click(1972,995)
        click(1972,995)
        sleep(1500)
        click(520,1720)
        sleep(1000);
        click(760,1970)
        sleep(1500);
        click(320,1310)
        sleep(1500);
    }
}
function findteam(img,y){//邀请队友
    img = img || captureScreen()
    y = y || 150;
    while(y<756){
        images.save(captureScreen(),'./img.jpg','jpg',100)
        var img = images.read('./img.jpg')
        var perm = colors.toString(images.pixel(img, 2230, y+80))
        if(perm == '#ff244d7f'){
            othr = images.clip(img, 1835, y, 420, 30)        
            msg = Baidu_OCR(othr)
            othr.recycle()
            log(msg);
            var pos = msg.indexOf("匹配");
            if(pos != -1){
                click(2230, y+80)
            }
        }
        if(colors.toString(images.pixel(img, 2230, y+80)) == '#ff0f1e2e'){
            click(1350,760)
        }
        y+=150
        if(colors.toString(images.pixel(img, 126, 1074)) == '#ff1c2840'){
            click(1350,770)
        }
    }
}
function invite(){//房内邀请
    images.save(captureScreen(),'./img.jpg','jpg',100)
    var img = images.read('./img.jpg')
    if(colors.toString(images.pixel(img, 170, 205)) == '#ffb64b42'){
        click(157,200)//打开邀请
        sleep(500)
        click(1765,301)//发送邀请
        sleep(500)
        click(1468,696)//接受邀请
        sleep(500)
        click(1747,112)//关闭邀请
    }
}

function matchteams(){//匹配
    var res = null
    var n = 0
    while(res == null){
        images.save(captureScreen(),'./img.jpg','jpg',100)
        var img = images.read('./img.jpg')
        var img = captureScreen()
        colors.toString(images.pixel(img, 1250, 50))
        if((colors.toString(images.pixel(img, 1250, 50))) == '#fff9f2ff'){
            break;
        }
        
        invite()
        if(colors.toString(images.pixel(img, 1275, 970)) == '#ff917047'){
            break;
        }   
        var temp = images.read('/storage/emulated/0/Pictures/测试/匹配成功.jpg')
        res = findImage(img, temp,{
            region: [1000, 150],
            threshold: 0.8
        });
        n++
        log(n)
        
    }
    click(1170,850)//确认
    sleep(200)
    click(1170,850)

}
function cnfrm2(){//选英雄界面检测
    var res = null
    while(res == null){
        var img = captureScreen()
        var temp = images.read('/storage/emulated/0/Pictures/测试/确定.jpg')
        res = findImage(img, temp,{
            region: [1950, 950],
            threshold: 0.5
        });
        img.recycle()
        temp.recycle()
        log(res)
    }

}

function pic2(){//选英雄
    images.save(captureScreen(),'./img.jpg','jpg',100)
    var img = images.read('./img.jpg')
    var temp = images.read('/storage/emulated/0/Pictures/测试/李信.jpg')
    var res = findImage(img, temp,{
        region: [0, 50],
        threshold: 0.9});
    if(res){
        click(164,611)//李信
        sleep(200)
        click(164,611)//李信
        sleep(500)
        click(2150,1000)//确定
        sleep(200)
        click(2150,1000)//确定
    }
}
function gamego(){//日强 投降
    sleep(10000)
    captureScreen('./img.jpg')
    var img = images.read('./img.jpg')
    // while(colors.toString(images.pixel(img, 1380,980)) != '#ffbaba0d'){
    //     sleep(5000)
    // }
    sleep(5000)
    while(colors.blue(images.pixel(img, 1380,980))-13<10){  
        swipe(345,845,45,845,1000)//日强
        sleep(400)
        click(266,423)//买装备
        sleep(500)
        click(2240,75)//设置
        sleep(500)
        click(1524,918)//发起投降
        sleep(500)
        click(2025,107)//关闭设置
        sleep(1500)
    }
}
function backteam(){//返回队伍
    sleep(20000);
    click(1180,990);
    sleep(10000);
    click(1180,990);
    sleep(1500);
    click(1310,970);
}
function mianfun(){
    lunch()
    login()
    close()
    takethings()
    teamsite()
    sentmsg()
}
mianfun()

// login()
// sleep(10000)
// close()
// takethings()
// teamsite()
// findteam()
//cnfrm2()
// matchteams()
// mianfun()
// sentmsg()
// matchteams()