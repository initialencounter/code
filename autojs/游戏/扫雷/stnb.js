var st_arr = []

function compute(){
for (var i=1; i<11; i++){
    var target = id('content_layout').drawingOrder(i).findOne()
    var time = parseFloat(target.child(1).text())
    var bvs = parseFloat(target.child(2).text())
    if (target.child(0).text()=='初级'){
        var cont = 47.229
    }
    else if (target.child(0).text()=='中级'){
        var cont = 153.73
    }
    else{
        var cont = 435.001
    }
    var st = cont/((time**1.7)/(time*bvs))
    st_arr.push(String(time)+' / '+String(st).slice(0,5))
}
log(st_arr)
}
// var path = "./test.js";
// if (!files.exists(path)) {
//     toast("脚本文件不存在: " + path);
//     exit();
// }
var window = floaty.window(
    <frame gravity="center_vertical">
         <vertical>
        <button id="action" text="计算" w="90" h="50" bg="#33ffffff"/>
        <text id = 't0' text='null' w="300" h="37" textColor="green" />
        <text id = 't1' text='null' w="300" h="37" textColor="green" />
        <text id = 't2' text='null' w="300" h="37" textColor="green" />
        <text id = 't3' text='null' w="300" h="37" textColor="green" />
        <text id = 't4' text='null' w="300" h="37" textColor="green" />
        <text id = 't5' text='null' w="300" h="37" textColor="green" />
        <text id = 't6' text='null' w="300" h="37" textColor="green" />
        <text id = 't7' text='null' w="300" h="37" textColor="green" />
        <text id = 't8' text='null' w="300" h="37" textColor="green" />
        <text id = 't9' text='null' w="300" h="37" textColor="green" />
        </vertical>
    </frame>
);

setInterval(() => {}, 1000);

var execution = null;

//记录按键被按下时的触摸坐标
var x = 0,
    y = 0;
//记录按键被按下时的悬浮窗位置
var windowX, windowY;
//记录按键被按下的时间以便判断长按等动作
var downTime;

window.action.setOnTouchListener(function(view, event) {
    switch (event.getAction()) {
        case event.ACTION_DOWN:
            x = event.getRawX();
            y = event.getRawY();
            windowX = window.getX();
            windowY = window.getY();
            downTime = new Date().getTime();
            return true;
        case event.ACTION_MOVE:
            //移动手指时调整悬浮窗位置
            window.setPosition(windowX + (event.getRawX() - x),
                windowY + (event.getRawY() - y));
            //如果按下的时间超过1.5秒判断为长按，退出脚本
            if (new Date().getTime() - downTime > 1500) {
                exit();
            }
            return true;
        case event.ACTION_UP:
            //手指弹起时如果偏移很小则判断为点击
            if (Math.abs(event.getRawY() - y) < 5 && Math.abs(event.getRawX() - x) < 5) {
                onClick();
            }
            return true;
    }
    return true;
});
window.setPosition(650,100)
function onClick() {
    if (window.action.getText() == '计算') {
        threads.start(function () {
            compute();
        })
        window.action.setText('计算完成');
    } else {
        window.t0.setText(st_arr[0])
        window.t1.setText(st_arr[1])
        window.t2.setText(st_arr[2])
        window.t3.setText(st_arr[3])
        window.t4.setText(st_arr[4])
        window.t5.setText(st_arr[5])
        window.t6.setText(st_arr[6])
        window.t7.setText(st_arr[7])
        window.t8.setText(st_arr[8])
        window.t9.setText(st_arr[9])

        window.action.setText('计算');
    }
}