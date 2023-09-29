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
var img = captureScreen()
// var point = findColor(img, "#ff0000", {
//     region: [400, 400, 200, 200],
//     threshold: 4
// });
// if(point){
//     log('1')
//     log(point.x)
// }
// img.recycle()
function matchteams(){//匹配
    var res = null
    while(res == null){
        if((colors.toString(images.pixel(img, 1250, 50))) == '#fff9f2ff'){
            teamsite()
            // sentmsg()
            while(teamcheck() < 4){
                findteam()
            } 
        }
        if((colors.toString(images.pixel(img, 170, 205))) == '#ffb64b42'){////////           
            click(157,200)//打开邀请
            sleep(500)
            click(1765,301)//发送邀请
            sleep(500)
            click(1468,696)//接受邀请
            sleep(500)
            click(1747,112)//关闭邀请
            if(hhcheck){//房主检测
                // sentmsg()
                while(teamcheck() < 4){
                    findteam()
                }
                // matchteams()
            
            }else{
                // sentmsg()
                // matchteams()
            }
            
        }
        var img = captureScreen()
        var temp = images.read('/storage/emulated/0/Pictures/测试/匹配成功.jpg')
        res = findImage(img, temp,{
            region: [1000, 150],
            threshold: 0.5
        });
        img.recycle()
        temp.recycle()
        
    }
    click(1170,850)
    sleep(200)
    click(1170,850)

}

// log(colors.toString(images.pixel(img1, 1250, 50)))
log(colors.toString(images.pixel(img, 1250, 50)))
log(colors.toString(images.pixel(img, 1250, 50)))









// function Baidu_OCR(imgFile) {
//     access_token = http.get("https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=YIKKfQbdpYRRYtqqTPnZ5bCE&client_secret=hBxFiPhOCn6G9GH0sHoL0kTwfrCtndDj").body.json().access_token;
//     url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic" + "?access_token=" + access_token;
//     imag64 = images.toBase64(images.read(imgFile));
//     res = http.post(url, {headers: {'Content-Type': 'application/x-www-form-urlencoded'},image: imag64,image_type: "BASE64",language_type:"JAP"});
//     str = JSON.parse(res.body.string()).words_result.map(val => val.words).join('\n');
//     return str;
// }

// imgFile = "/storage/emulated/0/Pictures/Screenshots/Screenshot_20210808_074249_com.tencent.tmgp.sgame.jpg";
// log(Baidu_OCR(imgFile));
