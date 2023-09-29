events.observeKey();
//监听音量上键按下
events.onKeyDown("volume_up", function(event){
    click(159,452)
    sleep(100)
    click(1647,932)
    sleep(100)
    click(1958,874)
    sleep(100)
    click(2021,103)
    sleep(100)
    click(274,443)
});
//监听菜单键按下
// events.onKeyDown("menu", function(event){
//     toast("菜单键被按下了");
//     exit();
// });