app.startActivity({
    action : 'VIEW',
    packageName : 'com.wisedu.cpdaily',
    className : 'com.wisorg.wisedu.home.ui.HomeActivity',
    root : true
});

id("tv_tab_title").className("android.widget.TextView").text("消息").findOne().parent().parent().click();
id("rc_item_conversation").findOne().click();
id("lv_app_msg").findOne().children().forEach(child => {
    var target = child.findOne(id("message_item"));
    target.click();
    });
var bul = true
for(var i=0; i<16; i++){
    if(bul == false){
        break
    }
    for(var j=0; j<59; j++){
        var x = i+''
        var y = j+''
        if(x.length<2){
            x = '0'+i
        }           
        if(y.length<2){
            y = '0'+j
        }
        log('今天 '+x+':'+y)
        var uiobj = id('tv_time').text('今天 '+x+':'+y)
        if(uiobj.exists()){
            var xx = uiobj.findOne().parent().bounds().centerX()+'';
            var yy = uiobj.findOne().parent().bounds().centerY()+'';
            shell('input tap '+xx+' '+yy,true)
            bul = false
            break
        }
    }
    log(i)
}
