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
// images.save(captureScreen(),'./img.jpg','jpg',100)
// var img = images.read('./img.jpg')
// var temp = images.read('/storage/emulated/0/脚本/局内操作/小地图头像.jpg')
// var res = findImage(img, temp,{
//     region: [40, 0, 360, 360],
//     threshold: 0.8
// });
// log(res)
// //导入插件
// captureScreen('./img.jpg')
// ocr = $plugins.load("com.hraps.ocr")
// //导入需识别的图片，请自行输入图片路径
// img = images.read("./img.jpg")
// //识别图片
// results = ocr.detect(img.getBitmap(),1)
// console.info("过滤前结果数："+results.size())
// //识别结果过滤
// results = ocr.filterScore(results,0.5,0.5,0.5)
// //输出最终结果
// for(var i=0;i<results.size();i++){
//     var re = results.get(i)
//     log("结果:"+i+"  文字:"+re.text)//+"  位置:"+re.frame+"  角度类型:"+re.angleType)
//     // log("区域置信度:"+re.dbScore+"  角度置信度:"+re.angleScore+"  文字置信度:"+re.crnnScore+"\n")
// }
// // var re = results.get(0)
// // log(re.text)
// img.recycle()