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
// var i = 1
// while(i<11){
function dw(){
    captureScreen('./img.jpg')
var img = images.read('./img.jpg') 
var temp = images.read('/storage/emulated/0/脚本/局内操作/小地图头像.jpg')
var res = findImage(img, temp,{
    region: [40, 0, 360, 360],
    threshold: 0.5
})
log(res)

img.recycle()
temp.recycle()
}

// //11 22 36 51 64 76 90 103 117 130
//8 19 31 43 55 65 77 89 100 113

// swipe(345,845,645,845,5000)//右
// swipe(345,845,45,845,1000)//左
// swipe(345,845,345,545,1000)//上
// swipe(345,845,345,1145,1000)//下

// var 狼 = '{ '

// for(var i = 186; i<202; i++){
//     狼 = 狼+(i+":"+116+",")
// }
// 狼 = 狼+' }'
// log(狼)
// var obj =eval('('+狼+')')
// log(obj[196])

// 狼 116 186-201   { '186':'116','187':'116','188':'116','189':'116','190':'116','191':'116','192':'116','193':'116','194':'116','195':'116','196':'116','197':'116','198':'116','199':'116','200':'116','201':'116', } 

// var obj = JSON.parse('{ "name":"ez", "age":10, "sex":"man" }');//使用内置的JSON对象
// var obj =$.parseJSON('{ "name":"ez", "age":10, "sex":"man" }') //json字符串转json对象的jQuery方式
// var obj =eval('('+jsonStr+')')
//启用按键监听


captureScreen('./img.jpg')
var img = images.read('./img.jpg')
while(Math.abs(colors.blue(images.pixel(img, 1380,980))-13)<10){
    img.recycle()  
    swipe(345,845,45,845,1000)//日强
    sleep(400)
    click(266,423)//买装备
    sleep(500)
    click(2240,75)//设置
    sleep(500)
    click(1524,918)//发起投降
    sleep(500)
    click(2025,107)//关闭设置
    sleep(15000)
    captureScreen('./img.jpg')
    var img = images.read('./img.jpg')
}
img.recycle()
// log(Math.random()*10)
