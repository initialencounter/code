// var jstr = files.read('./yanzhi.txt')
// var str = '{'+jstr+'}'
// var obj = eval('(' + str + ')');
// var imgname = files.listDir('./img/')
// log(obj)
// log(imgname)
// for(var i = 0; i<imgname.length;i++){
//     var key_ = imgname[i].toString()
//     log(obj[key_])
// }


// var ak = '8kawU4KnlvCMIZNW7wgi7rvp';//你的人脸识别ak
// var sk = 'DdSCPGAe3100DybVWoq1BbdPsvrFLIic';//你的人脸识别sk
// var access_token = http.get("https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + ak + "&client_secret=" + sk).body.json().access_token;
// log(access_token)
// var sh = new Shell(true)
// sleep(500)
// threads.start(function () {
//     sleep(2000)
//     sh.exec('input tap 850 1250')
// })
// alert('性别:female 年龄:26 颜值:50.66 ')
// sleep(500)
// sh.exit()

// var a = app.launchPackage('com.ss.android.ugc.aweme')
// // var a = app.launchPackage('com.huawei.camera')

// log(a)1
    var sh = new Shell(true)
    sleep(500)
    sh.exec('input tap 985 1450')//评论
        setClip('颜值：')
        sleep(500)
        sh.exec('input tap 555 2130')
        sleep(500)
        sh.exec('input keyevent 279')
        sleep(500)
        // sh.exec('input tap 1000 1170')
        sleep(500)
        sh.exec('input tap 500 200')
        sleep(500)
        sh.exec('input tap 500 200')
    sleep(500)
    sh.exit()



