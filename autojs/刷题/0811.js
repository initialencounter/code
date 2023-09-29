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
function Baidu_OCR(img){//调用API
    access_token = http.get("https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=YIKKfQbdpYRRYtqqTPnZ5bCE&client_secret=hBxFiPhOCn6G9GH0sHoL0kTwfrCtndDj").body.json().access_token;
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic" + "?access_token=" + access_token;
    imag64 = images.toBase64(img,'jpg',50);
    res = http.post(url, {headers: {'Content-Type': 'application/x-www-form-urlencoded'},image: imag64,image_type: "BASE64",language_type:"JAP"});
    str = JSON.parse(res.body.string()).words_result.map(val => val.words).join('');
    return str;
}
events.observeKey();
events.onKeyDown('volume_up', function(event){
    var img = images.clip(captureScreen(),90,680,900,530)
    ques = Baidu_OCR(img);
    img.recycle()
    toastLog(ques)
    // var url ='http://m.syiban.com/search/index/init.html?is_wap=1&modelid=1&q='+ques
    // res = http.get(url, 
    //     {headers:{
    //         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36}'}
    //     })
    // var html = res.body.string();
    // ans = html.indexOf('答案：')
    // ans2 = html.substring(ans+3,ans+10);
    // log(ans2)
    // var kjian
    // if(kjian = text(ans2).findOne().parent()){
    //     kjian.click
    // }
});