// function ctjc(){
//     if(!requestScreenCapture()){
//         toast("请求截图失败");
//         exit
//     }
//     var x = 351;//351 619 887 1155 1423
//     var y = 573;
//     var n=0; m=0;
//     var ma = images.pixel(captureScreen(), 1287, 970);
//     if (ma == '#ff88714b'){
//         while(n<5){
//             var c = images.pixel(captureScreen(), x, y);
//             var f = "";
//             f = colors.toString(c).substring(3,4);
//             if(f=='f'){
//                 m+=1
//             }
//             n++
//             x+=268
//         }
//         if(m>3){
//             log('ok')
//         } 
//     }
// }
// function jdcb(){
//     click(1156,836)//确认
//     sleep(500)
//     click(157,200)//打开邀请
//     sleep(500)
//     click(1765,301)//发送邀请
//     sleep(500)
//     click(1468,696)//接受邀请
//     sleep(500)
//     click(1747,112)//关闭邀请
//     sleep(500)
//     click(164,611)//李信
//     sleep(500)
//     click(2199,1035)//确定
//     sleep(500)
//     swipe(345,845,45,845,1000)//日强
//     sleep(500)
//     click(266,423)//买装备
//     sleep(500)
//     click(2240,75)//设置
//     sleep(500)
//     click(1524,918)//发起投降
//     sleep(500)
//     click(2025,107)//关闭设置
//     sleep(500)
//     click(1155,977)//继续
//     sleep(500)
//     click(1206,983)//返回房间
// }

// while(true){
//     ctjc();
//     jdcb();
// }
// function Baidu_OCR(img) {
//     access_token = http.get("https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=YIKKfQbdpYRRYtqqTPnZ5bCE&client_secret=hBxFiPhOCn6G9GH0sHoL0kTwfrCtndDj").body.json().access_token;
//     url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic" + "?access_token=" + access_token;
//     imag64 = images.toBase64(img,'jpg',50);
//     res = http.post(url, {headers: {'Content-Type': 'application/x-www-form-urlencoded'},image: imag64,image_type: "BASE64",language_type:"JAP"});
//     str = JSON.parse(res.body.string()).words_result.map(val => val.words).join('\n');
//     return str;
// }





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
// var img = captureScreen()
// var y = 150





// function findteam(img,y){
//     while(y<756){
//         othr = images.clip(img, 1835, y, 420, 30)
//         var perm = colors.toString(images.pixel(img, 2230, y+80))
//         // img.recycle()
//         images.save(othr, "/storage/emulated/0/Pictures/Screenshots/1.jpg", "jpg", 100);
//         othr.recycle()
//         imgFile = "/storage/emulated/0/Pictures/Screenshots/1.jpg";
//         msg = Baidu_OCR(imgFile)
//         log(msg);
//         var pos = msg.indexOf("匹配");
//         if(pos != -1){
//             if(perm == '#ff244d7f'){
//                 click(2230, y+80)
//             }
//         }
//         if(colors.toString(images.pixel(img, 2230, y+80)) == '#ff0f1e2e'){
//             click(1350,760)
//         }
//         y+=150
//     }
// }
// findteam(img,y)
// log(colors.toString(images.pixel(othr, 200, 10)))
// log(colors.toString(images.pixel(img, 2230, 230)))
// log(colors.toString(images.pixel(img, 2230, 380)))
// log(colors.toString(images.pixel(img, 2230, 530)))
// log(colors.toString(images.pixel(img, 2230, 680)))
// log(colors.toString(images.pixel(img, 2230, 830)))
// log(colors.toString(images.pixel(img, 382,515)))
// log(colors.toString(images.pixel(img, 650, 515)))
// log(colors.toString(images.pixel(img, 918, 515)))
// log(colors.toString(images.pixel(img, 1186, 515)))
// log(colors.toString(images.pixel(img, 1454, 515)))
// log(colors.toString(images.pixel(img, 382, 420)))
// log(colors.toString(images.pixel(img, 650, 420)))
// log(colors.toString(images.pixel(img, 918, 420)))
// log(colors.toString(images.pixel(img, 1186, 420)))
// log(colors.toString(images.pixel(img, 1454, 420)))
// function tck(img){
//     var x = 382;
//     var n = 0;
//     while(x<1455){
//         // var img = captureScreen()
//         if(colors.toString(images.pixel(img, x, 515)) == '#ff233a5b'){
//             n++;
//             x+=268;
//         }
//     }
//     // img.recycle()
//     return n
// }
// function qr(){
//     var pos = -1;
//     while(pos == -1){
//         img = images.clip(captureScreen(),1050,180,230,70)
//         msg = Baidu_OCR(img)
//         pos = msg.indexOf('匹配成功')
//         log(pos)

//     }
//     click(1180,830)
// }
// function pic(){
//     var pos = -1;
//     while(pos == -1){
//         img = images.clip(captureScreen(),2080,980,70,45)
//         msg = Baidu_OCR(img)
//         pos = msg.indexOf('确定')
//         log(pos)

//     }
//     click(164,611)//李信
//     sleep(500)
//     click(2199,1035)//确定
//     sleep(500)
// }
// qr()
// pic()
// log(tck(img))
// var imsge = captureScreen()
// var temp = images.clip(imsge, 1055, 185, 230, 125)
// images.save(temp, '/storage/emulated/0/Pictures/测试/匹功.jpg', 'jpg', 100)
// imsge.recycle()
// temp.recycle()
// function gamego(){
//     while(colors.toString(images.pixel(img, 1380,980)) != '#ffbaba0d'){
//         sleep(5000)
//     }
//     sleep(5000)
//     while(colors.toString(images.pixel(img, 1380,980)) == '#ffbaba0d'){  
//         swipe(345,845,45,845,1000)//日强
//         sleep(400)
//         click(266,423)//买装备
//         sleep(500)
//         click(2240,75)//设置
//         sleep(500)
//         click(1524,918)//发起投降
//         sleep(500)
//         click(2025,107)//关闭设置
//         sleep(1500)
//     }
// }
// function backteam(){
//     sleep(20000);
//     click(1180,990);
//     sleep(10000);
//     click(1180,990);
//     sleep(1500);
//     click(1310,970);
// }
// function sentmsg(){
//     for(var i=1; i<6; i++){
//         var nam1;
//         var nam2;
//         var nam3;
//         click(1972,995)
//         sleep(3000)
//         if(nam1 = id("text1").className("android.widget.TextView").text("掉胜率"+i).findOne().parent()){
//             nam1.click()
//         }
//         sleep(2000);
//         if(nam2 = id("dialogRightBtn").findOne()){
//             nam2.click()
//         }
//         sleep(2000);
//         if(nam3 = desc("返回王者荣耀按钮").findOne()){
//             nam3.click()
//         }
//         sleep(3000);
//     }
// }
// // sentmsg()
// function invite(){
//     if(colors.toString(images.pixel(img, 170, 205)) == '#ffb64b42'){
//         click(157,200)//打开邀请
//         sleep(500)
//         click(1765,301)//发送邀请
//         sleep(500)
//         click(1468,696)//接受邀请
//         sleep(500)
//         click(1747,112)//关闭邀请
//     }
// }

//踢掉未准备