
// while(1){
// swipe(345,845,345,1135,200)
// sleep(10)
// click(1218,963)
// swipe(345,845,345,545,180)
// sleep(10)
// click(1218,963)
// swipe(345,845,45,1135,180)
// sleep(10)
// click(1218,963)
// swipe(345,845,645,1135,180)
// sleep(10)
// click(1218,963)
// sleep(10)
// click(1218,963)
// sleep(90)
// }
var ra = new RootAutomator();

for(i=0; i<5; i++){
    //让"手指1"点击位置(100, 100)
    ra.tap(1218, 963, 1);
    sleep(1000)
    //让"手指2"
    ra.swipe(260,434,122,515,1000,2)
    sleep(1000)
}
ra.exit();