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
var tiku = storages.create('2911583893')
function wenti(){
    var wenti = className("android.view.View").depth("11").drawingOrder("0").indexInParent("2").findOnce().text()
    //对获取的题目进行处理，去除所有特殊字符
    pattern=/[`~!@#$^&*()=|{}':;'“”,\\\[\]\.<>\/?~！@#￥……&*（）——|{}【】'；：""'。，、？\s]/g;
    wenti = wenti.replace(pattern,"")  
    return wenti
}


function obj(){//选项文本数组
    var obj = []
    className("android.view.View").depth("14").drawingOrder("0").indexInParent("2").find().forEach(function(tv){
        obj.push(tv.text())
    }) 
    return obj
}

function objnum(){//选项个数
    var obj1 = className("ListView").depth("11").drawingOrder("0").indexInParent("4").findOnce().childCount()
    return obj1
}

function clickab(){//选项坐标数组
    var xy = []
    className("android.view.View").depth("14").drawingOrder("0").indexInParent("2").find().forEach(function(tv){
        xy.push(tv.bounds().centerX())
        xy.push(tv.bounds().centerY())
    })
    return xy
}

function tobj(){//判断选项对错
    var img1 = images.read('./img1.jpg')
    var img2 = images.read('./img2.jpg')
    var xy = clickab()
    var da = []
    if(objnum()==4){
        if(colors.toString(images.pixel(img1, xy[0], xy[1])) == colors.toString(images.pixel(img2, xy[0], xy[1]))){
            da.push(1)
        }
        if(colors.toString(images.pixel(img1, xy[2], xy[3])) == colors.toString(images.pixel(img2, xy[2], xy[3]))){
            da.push(2)
        }
        if(colors.toString(images.pixel(img1, xy[4], xy[5])) == colors.toString(images.pixel(img2, xy[4], xy[5]))){
            da.push(3)
        }
        if(colors.toString(images.pixel(img1, xy[6], xy[7])) == colors.toString(images.pixel(img2, xy[6], xy[7]))){
            da.push(4)
        }

    }else if(objnum()==3){
        if(colors.toString(images.pixel(img1, xy[0], xy[1])) == colors.toString(images.pixel(img2, xy[0], xy[1]))){
            da.push(1)
        }
        if(colors.toString(images.pixel(img1, xy[2], xy[3])) == colors.toString(images.pixel(img2, xy[2], xy[3]))){
            da.push(2)
        }
        if(colors.toString(images.pixel(img1, xy[4], xy[5])) == colors.toString(images.pixel(img2, xy[4], xy[5]))){
            da.push(3)
        }

    }else if(objnum()==2){
        if(colors.toString(images.pixel(img1, xy[0], xy[1])) == colors.toString(images.pixel(img2, xy[0], xy[1]))){
            da.push(1)
        }
        if(colors.toString(images.pixel(img1, xy[2], xy[3])) == colors.toString(images.pixel(img2, xy[2], xy[3]))){
            da.push(2)
        }

    }
    return da
}
function final(){
    var da = tobj()
    var obj = className("android.view.View").depth("14").drawingOrder("0").indexInParent("2").findOnce().text()
    if(da.length <2){//只有一个点颜色改变，选项一正确
        // tiku.push(wenti(),obj[0])//写入储存
        log(obj[0])
    }else{//两个颜色改变
        var n = da[1]//改变的选项即为正确答案
        log(obj[n])
        // tiku.push(wenti(),obj[n])
}
}
// images.save(captureScreen(),'./img1.jpg', "jpg", 100)//最初的图片 
// sleep(500)
// images.save(captureScreen(),'./img2.jpg', "jpg", 100)//最后的图片
// final()//存答案


function main(){
    var wt = wenti()
    if(tiku.contains(wt)){//找到题目
        var txt = tiku.get(wt)
        var XY = className("android.view.View").depth("14").text(txt).findOnce().bounds()
        var ram = Math.ceil(Math.random()*100);
        log(XY.centerX()+ram,XY.centerY()+ram)
        var tr = Math.ceil(Math.random()*1000);
        sleep(2000+tr)
    }else{
        images.save(captureScreen(),'./img1.jpg', "jpg", 100)//最初的图片 
        var XY2 = clickab()
        var tr = Math.ceil(Math.random()*1000);
        var ram = Math.ceil(Math.random()*100);
        log(XY2[0]+ram,XY2[1]+ram)
        sleep(500)
        images.save(captureScreen(),'./img2.jpg', "jpg", 100)//最后的图片
        final()//存答案
        var ram = Math.ceil(Math.random()*100); 
        click(535+ram,1735+ram)
        // img1.recycle()
        // img2.recycle()
        sleep(2000+tr)
        

    }
}
function obj(){//选项文本数组
    var obj = []
    className("android.view.View").depth("14").drawingOrder("0").indexInParent("2").find().forEach(function(tv){
        obj.push(tv.text())
    }) 
    return obj
}
function clickab(){//选项坐标数组
    var xy = []
    className("android.view.View").depth("14").drawingOrder("0").indexInParent("2").find().forEach(function(tv){
        xy.push(tv.bounds().centerX())
        xy.push(tv.bounds().centerY())
    })
    return xy
}
log(clickab())
