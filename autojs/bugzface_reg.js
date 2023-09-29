function Face_recognition(img, access_token) {
    var url = "https://aip.baidubce.com/rest/2.0/face/v3/detect" + "?access_token=" + access_token;
    var image64 = images.toBase64(img);
    if (img) {
        var res = http.post(url, {
            headers: {
                'Content-Type': 'application/json; charset=UTF-8'
            },
            'image': image64,
            'image_type': 'BASE64',
            'face_field': 'gender,age,beauty'
        });
        var str = JSON.parse(res.body.string());
        if (str['error_msg'] == 'pic not has face') {
            toastLog(".没有检测到人脸！");
            var num = 0
        } else if (str['error_msg'] == 'SUCCESS') {
            var gender = str['result']['face_list'][0]['gender']['type']
            var num = parseInt(str['result']['face_list'][0]['beauty'])
            var age = str['result']['face_list'][0]['age'] + '颜值:'
            // threads.start(function () {
            //     sleep(1500)
            //     sh.exec('input tap 850 1250')//关闭弹窗
            // })
            // log(gender + age + num)
            // alert(gender + age + num)
            toastLog(age + num)
            if (gender == 'male') {
                num = 0 - num
            }
        }
        
    }
    return num
}

function flw(yanzhi) {
    var sh = new Shell(true)
    sh.exec('input tap 985 1066')//关注
    sleep(500)
    sh.exec('input tap 988 1239')//点赞
    sleep(500)
    sh.exec('input tap 985 1450')//评论
    setClip('颜值：' + yanzhi)
    sleep(500)
    sh.exec('input tap 555 2130')
    sleep(500)
    sh.exec('input keyevent 279')
    sleep(500)
    sh.exec('input tap 1000 1170')
    sleep(500)
    sh.exec('input tap 1000 670')
    sleep(500)
    sh.exit()
}

function initdy() {
    app.launchPackage('com.ss.android.ugc.aweme')
    sleep(5000)
    threads.start(function () {
        var beginBtn;
        if (beginBtn = classNameContains("Button").textContains("立即开始").findOne(2000)) {
            beginBtn.click();
        }
    })
    if (!requestScreenCapture()) {
        toast("请求截图失败");
        exit
    }
}


function main() {
    var ak = '8kawU4KnlvCMIZNW7wgi7rvp';//你的人脸识别ak
    var sk = 'DdSCPGAe3100DybVWoq1BbdPsvrFLIic';//你的人脸识别sk
    var access_token = http.get("https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + ak + "&client_secret=" + sk).body.json().access_token;
    var sh = new Shell(true)
    while (true) {
        var date = new Date()
        var img1 = captureScreen()
        var img = images.grayscale(img1)
        var data_str = date.toString()
        var reg = new RegExp(' ', 'g')
        var name_ = data_str.replace(reg, '').slice(3, 20) + '.jpg'
        var yanzhi = Face_recognition(img, access_token)
        img.recycle()
        if (yanzhi > 65) {
            flw(yanzhi)
            images.save(img1, './img/' + name_)
            img1.recycle()
            var conten = "'" + name_ + "' : " + yanzhi + ",\n"
            files.append('./yanzhi.txt', conten)
        }
        sh.exec('input swipe 650 1500 900 400 200')//下一条视频
        sleep(5000)
        sh.exit()
    }
}

initdy()
main()