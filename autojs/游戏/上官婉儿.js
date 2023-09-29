events.observeKey();
//监听音量上键按下
events.onKeyDown("volume_up", function(event){
    蹲草();
});
function 中路(){
    click(2010,630)//3
    sleep(50)
    swipe(1810,750,1980,570,200)//2
    sleep(50)
    swipe(1690,950,1920,710,200)//1
    sleep(50)
    click(1520,960)//净化
    sleep(50)
    swipe(345,845,420,705,700)
    sleep(50)
    swipe(345,845,162,1050,600)
    sleep(50)
    swipe(345,845,420,805,300)
    sleep(1700)
    click(2000,420)//金身
}

function 上路(){
    click(2010,630)//3
    sleep(50)
    swipe(1810,750,1810,400,200)//2
    sleep(50)
    swipe(1690,950,1690,600,200)//1
    sleep(50)
    swipe(345,845,345,545,700)
    sleep(50)
    click(1520,960)//净化
    sleep(50)
    swipe(345,845,345,1145,600)
    sleep(50)
    swipe(345,845,345,545,300)
    sleep(1700)
    click(2000,420)
}
function 下路(){
    click(2010,630)//3
    sleep(50)
    swipe(1810,750,2110,750,200)//2
    sleep(50)
    swipe(1690,950,2090,960,200)//1
    sleep(50)
    swipe(345,845,645,845,700)
    sleep(50)
    click(1520,960)//净化
    sleep(50)
    swipe(345,845,45,845,600)
    sleep(50)
    swipe(345,845,645,845,300)
    sleep(1700)
    click(2000,420)
}
// click(1880,660)
function 强化普(){
for(var i=1; i<11; i++){
swipe(1880,660,2090,233,450)//3
sleep(90)
click(2000,900)//2380 
sleep(140)

press(1740,780,450)//2
sleep(90)
click(2000,900)//2380 
sleep(140)

swipe(1680,950,2090,233,450)//1
sleep(90)
click(2000,900)//2380 
sleep(130)
}
}
function 蹲草(){
    for(var i=1; i<2; i++){
        press(1880,660,1010)//3
        sleep(90)
        click(2000,900)//a
        sleep(550)
        press(1740,780,200)//2
        sleep(90)
        click(2000,900)//a
        sleep(550)
        press(1680,950,1010)//1
        // click(1520,960)//净化
        
    }
}
// 蹲草()
// for(var i=1; i<10; i++){
// // press(1740,780,200)//2
// click(2000,900)//a
// sleep(550)

// press(1680,950,1010)//1
// sleep(90)
// }
// 强化普()