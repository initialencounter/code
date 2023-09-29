// var sh = new Shell(true)
// sleep(200)
// app.startActivity({
//     action : 'VIEW',
//     packageName : 'com.duowan.kiwi',
//     className : 'com.duowan.kiwi.homepage.Homepage',
//     root : true
// })
// waitForActivity('com.duowan.kiwi.homepage.Homepage', 50)
// sh.exec('uiautomator dump /sdcard/脚本/xml1.xml')
// sleep(3000)
// sh.exit()
// var xml = files.read('/sdcard/脚本/xml1.xml')
// log(xml)


// var xml=XMLHttpRequest("GET","/sdcard/脚本/xml1.xml");
// var path="/hierarchy/node/index"
// code for IE
// if (window.ActiveXObject)
// {
// var nodes=xml.selectNodes(path);
// log(nodes)


// var xml = new XMLHttpRequest()
// xml.open('GET',"/sdcard/脚本/xml1.xml",false)
// var path="/hierarchy/node/index"
// var nodes=xml.selectNodes(path);
// log(nodes)

// re = new RegExp()
// var str="da  jia hao hao xue xi a";
// var reg=/\b[A-Z]{3}\b/ig;    //忽略大小写

// var line=reg.exec(str)
// log(line)// jia
// var x = 1018298
// log(Math.round())
// // click(650,120)
// var shift_list = className("android.view.View").text('手Q苹果区').findOne().bounds()

// swipe(shift_list.centerX(),shift_list.centerY(),shift_list.centerX(),(shift_list.centerY()-110),500)
// var bmid = className("android.view.View").text('虎牙北慕慕慕').findOne().bounds()
// let paint = new Paint()
// paint.setStyle(Paint.STYLE.FILL)
// paint.setColor(colors.RED)
// canvas.DrawRecr(bmid,paint)
"ui";
//ui布局为一块画布
ui.layout(
    <vertical>
        <canvas id="board"
        h = "*"
         w = "*"/>
    </vertical>
);

ui.board.on("draw", function(canvas) {  
    var paint = new Paint();
   //设置画笔为填充，则绘制出来的图形都是实心的
    paint.setStyle(Paint.Style.FILL);
   //设置画笔颜色为红色
    paint.setColor(colors.RED);
    //绘制一个从坐标(0, 0)到坐标(500, 500)的正方形
    canvas.drawRect(0, 0, 500, 500, paint);
  }) 