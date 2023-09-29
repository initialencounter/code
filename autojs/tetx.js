function jdcb(){
    click(1156,836)//确认
    sleep(500)
    click(157,200)//打开邀请
    sleep(500)
    click(1765,301)//发送邀请
    sleep(500)
    click(1468,696)//接受邀请
    sleep(500)
    click(1747,112)//关闭邀请
    sleep(500)
    click(164,611)//李信
    sleep(500)
    click(2199,1035)//确定
    sleep(500)
    swipe(345,845,45,845,1000)//日强
    sleep(500)
    click(266,423)//买装备
    sleep(500)
    click(2240,75)//设置
    sleep(500)
    click(1524,918)//发起投降
    sleep(500)
    click(2025,107)//关闭设置
    sleep(500)
    click(1155,977)//继续
    sleep(500)
    click(1206,983)//返回房间
}
function ctjc(){
    if(!requestScreenCapture()){
        toast("请求截图失败");
        exit
    }
    var x = 351;//351 619 887 1155 1423
    var y = 573;
    var n=0; m=0;
    var point = images.findColorInRegion(images, '#ff88714b', 1287, 970, 300,100 )
    var ma = images.pixel(captureScreen(), 1287, 970);
    // if (ma == '#ff88714b'){
    if (point){
        // while(n<5){
        //     var c = images.pixel(captureScreen(), x, y);
        //     var f = "";
        //     f = colors.toString(c).substring(3,4);
        //     if(f=='f'){
        //         m+=1
        //     }
        //     n++
        //     x+=268
        // }
        // if(m>3){
        //     log('ok')
        // } 
        log(1)
    }
}
function zs(n1,n2){
    if(!requestScreenCapture()){
        toast("请求截图失败");
        exit
    }
    sleep(2000);
    var x = n1;
    var y = n2;
    //获取在点(x, y)处的颜色
    var c = images.pixel(captureScreen(), x, y);
    //显示该颜色
    var msg = "";
    msg += "在位置(" + x + ", " + y + ")处的颜色为" + colors.toString(c);
    log(msg);
}

function qyzs(n2,n3,n4,n5,n6){
    if(!requestScreenCapture()){
        toast("请求截图失败");
        exit();
    }
    //指定在位置(100, 220)宽高为400*400的区域找色。
    //#75438a是编辑器默认主题的棕红色字体(数字)颜色，位置大约在第5行的"2000"，坐标大约为(283, 465)
    var point = findColor(captureScreen(),n2,n3,n4,n5,n6);
    log(point)
    if(point){
        log("x = " + point.x + ", y = " + point.y);
    }else{
        log("没有找到");
    }
}
// qyzs('#ff9a8356',0,0,2340,1080)
// zs(1250,1000)
// requestScreenCapture();
// var img = captureScreen();
// var point = findColor(img, "#ffdad7e5");
// if(point){
//     toast("找到红色，坐标为(" + point.x + ", " + point.y + ")");
// }
// log(point)
// zs(618,575)
// zs(887,573)
// zs(1155,573)
// zs(1423,573)
// requestScreenCapture();

// var img = captureScreen();
// var point = findColor(img, "#7b40c9");
// if(point){
//     toast("找到红色，坐标为(" + point.x + ", " + point.y + ")");
// }
// log(point)
// zs(187,274)
