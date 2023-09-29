function 启动(){
    launchApp('王者荣耀')
    toast('启动')
}
function 开始游戏(){
    click(1173,866)
    toast('开始游戏')
}
function 关闭弹窗(){
    click(2000,175)
    toast('关闭弹窗')
}
function 活动(){
    click(2200,350)
    toast('活动')
}
function 对战(){
    click(1000,800)
    toast('对战')
}
function 单挑(){
    click(1400,550)
    toast('1v1')
}
function 匹配(){
    click(800,520)
    toast('匹配')
}
function 确定(){
    click(1350,750)
    toast('确定')
}
function 确认(){
    click(1160,840);
    toast("确认");
}
function 向前(){//20秒
    for(i=0;i<=10;i++){//向前
        swipe(350,850,550,530,2000)
        toast('向前')
    }
}
function 向后(){//20秒
    for(i=0;i<10;i++){//向后
        swipe(350,850,150,1130,2000)
        toast('向后')
    }
}
function 向左(){//20秒
    for(i=0;i<10;i++){//向左
        swipe(350,850,150,530,2000)
        toast('向左')
    }
}
function 向右(){//20秒
    for(i=0;i<10;i++){//向右
        swipe(350,850,530,1130,2000)
        toast('向右')
    }
}
function 投降(){//0.5秒
    click(2240,70)//投降
    toast("设置")
    sleep(500)
    click(1400,940)//投降
    toast('投降')

}
function 转圈圈(){//4秒
    while(1){//转圈圈
        // swipe(350,850,550,530,1000)//前
        // swipe(350,850,550,1130,1000)//右
        // swipe(350,850,150,1130,1000)//后
        // swipe(350,850,150,530,1000)//左
        
        swipe(350,850,350,550,1100)//竖
        swipe(350,850,650,850,1000)
        swipe(350,850,350,1150,1000)
        swipe(350,850,50,850,1000)//横
        toast('转圈圈')
}
}
function 局内商店(){
    click(140,440)// 局内商店()
    toast('局内商店')
}
function 装备栏(){
    click(600,950)//装备方案
    click(1750,410)//使用装备方案三
    click(1750,610)//使用装备方案二
    click(1750,810)//使用装备方案三
    click(1830,145)//关闭装备方案
    click(830,950)//1
    click(990,950)//2
    click(1150,950)//3
    click(1310,950)//4
    click(1470,950)//5
    click(1630,950)//6
    click(1960,860)//出售
    click(430,270)//购买
    click(2020,90)//关闭商店
}
function 继续(){
    click(1180,990)
    toast('继续')
}
function 再来一局(){
    click(1300,970)
    toast("再来一局")
}
function coordinates(x,y){
    this.x=x
    this.y=y
    this.coordi=function(){
        click(this.x,this.y)
    }
}
var coordi1=new coordinates(830,950)
function 装备方案(){
    click(600,950)
    // toast('装备方案')
}
function 使用装备方案三(){
    click(1750,410)
    // toast('使用装备方案三')
}
function 使用装备方案二(){
    click(1750,610)
    // toast('使用装备方案二')
}
function 使用装备方案三(){
    click(1750,640)
    // toast('使用装备方案三')
}
function 关闭装备方案(){
    click(1830,145)
    // toast('关闭装备方案')
}
function 装备栏1(){
    click(830,950)//1
    // toast('装备栏1')
} 
function 装备栏2(){
    click(990,950)//2
    // toast('装备栏2')
}
function 装备栏3(){
    click(1150,950)//3
    // toast('装备栏3')
}
function 装备栏4(){
    click(1310,950)//4
    // toast('装备栏4')
}
function 装备栏5(){
    click(1470,950)//5
    // toast('装备栏5')
}
function 装备栏6(){
    click(1630,950)//6
    // toast('装备栏6')
}
function 出售(){
    click(1960,860)//出售
    // toast('出售')
}
function 购买(){
    click(280,460)//购买
    // toast('购买')
}
function 关闭商店(){
    click(2020,90)//关闭商店
    // toast('关闭商店')
}
function 换装备(){
    toast()
    局内商店()
    sleep(100)
    装备栏1
    sleep(100)
    出售()
    sleep(100)
    关闭商店()
    sleep(100)
    购买()
}
function 挂机(){
    启动()
    sleep(30000)
    开始游戏()
    sleep(20000)
    关闭弹窗()
    sleep(500)
    关闭弹窗()
    sleep(500)
    关闭弹窗()
    sleep(500)
    对战()
    sleep(500)
    单挑()
    sleep(500)
    匹配()
    sleep(500)
    确定()
    sleep(20000)
    var x=0
    while(x<14){
        再来一局()
        sleep(20000)
        确认()
        sleep(40000)
        var y=0
        while(y<60){
            转圈圈()
            y++
        }
        投降()
        sleep(20000)
        继续()
        sleep(20000)
        toast("任意位置")
        sleep(10000)
        继续()
        toast("任意位置")
        sleep(500)
        x++
    }
}
function hz(){
局内商店()
sleep(50)
装备方案()
sleep(100)
使用装备方案三()
sleep(50)
关闭装备方案()
sleep(50)
装备栏1()
sleep(50)
出售()
sleep(50)
装备栏2()
sleep(50)
出售()
sleep(50)
装备栏3()
sleep(50)
出售()
sleep(50)
装备栏4()
sleep(50)
出售()
sleep(50)
装备栏5()
sleep(50)
出售()
sleep(50)
装备栏6()
sleep(50)
出售()
sleep(50)
关闭商店()
sleep(50)
购买()
sleep(50)
购买()
sleep(50)
购买()
sleep(50)
购买()
sleep(50)
购买()
sleep(50)
购买()
}
"auto";

events.observeKey();
//监听音量下键弹起
events.onKeyDown("volume_down",function 装备栏(){
    hz()
}
    
);