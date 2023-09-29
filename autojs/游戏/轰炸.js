// threads.start(function () {
//     var beginBtn;
//         if (beginBtn = classNameContains("Button").textContains("立即开始").findOne(2000)) {
//             beginBtn.click();
//         }
//     })
// if(!requestScreenCapture()){
//     toast("请求截图失败");
//     exit
// }
// sleep(250)
// captureScreen('./img.jpg')
// var img = images.read('./img.jpg')
// if(Math.abs(colors.blue(images.pixel(img, 1380,980))-13)<10){

function junei(){//局内轰炸
    for(var i=0;i<5;i++){
        text = Math.random()
        click(2200,420)//气泡
        sleep(500)
        if(i==0){
            click(1800,820)
            sleep(500)
        }
        click(2080,820)//打字
        sleep(500)
        click(1400,470)//关闭键盘
        sleep(500)
        className("android.widget.EditText").setText(text)
        sleep(200)
        className("android.widget.Button").click()
        sleep(200)
        swipe(345,845,420,705,3000)
    }

}
// }
// else{
//     click(410,990)
//     sleep(500)
//     click(410,990)
//     sleep(500)
//     var text = ''
//     for(var i=0;i<11;i++){
//     click(410,990)
//     sleep(500)
//     click(1430,410)//关闭键盘
    
//     className("android.widget.EditText").setText(text)
//     className("android.widget.Button").click()
//     sleep(500)
//     click(1200,1000)
//     sleep(500)
//     text = Math.random()
//     }
// }