// function 震动(vibrate_time)
// {     
//     var vibrate_time = vibrate_time || 3000 
//     device.vibrate(vibrate_time);
// }
function 加速()
{
    click(260,250)
    id("ijk_layout_controller_cover_screen_btn").findOne().click()
    if(id("ijk_layout_controller_cover_rate_btn").text("1.0x").exists())
    {
        id("ijk_layout_controller_cover_rate_btn").text("1.0x").findOne().click()
    }
    if(id("ijk_layout_controller_cover_rate_btn").text("1.25x").exists())
    {
        id("ijk_layout_controller_cover_rate_btn").text("1.25x").findOne().click()
    }
    id("ijk_layout_controller_cover_back_btn").findOne().click()
}
var dy = 499
function 控件判断(){
    while(className("android.view.View").bounds(44,dy,676,dy+108).exists()==false){
        dy+=34
    }
}
function 选题()
{
    
    var a=className('android.widget.TextView').text('A')
    var b=className('android.widget.TextView').text('B')
    var c=className('android.widget.TextView').text('C')
    var d=className('android.widget.TextView').text('D')
    var a5=className('android.widget.TextView').text('A')
    
    a.click()
    b.click()
    c.click()
    d.click()
    var as = a5.findOne().text()
    var answer = as.split("")
    
    answer.splice(0,(0,1,2,3,4,5))
    log(answer)
    log(answer.length)
    a.click()
    b.click()
    c.click()
    d.click()
    var aa = answer.indexOf('A')
    var bb = answer.indexOf('B')
    var cc = answer.indexOf('C')
    var dd = answer.indexOf('D')
    if(aa != -1){
        a.click()
    }
    if(bb != -1){
        b.click()
    }
    if(cc != -1){
        c.click()
    }
    if(dd != -1){
        d.click()
    }
}
function 关闭弹窗()
{
    className("android.view.View").text("关闭").findOne().click()
}
function 弹窗检测()
{
if (className("android.view.View").text("弹题是为了帮助同学们巩固知识点，不会影响到大家作业和考试的成绩。").exists())
{
    sleep(3000)
    选题()
    关闭弹窗()
}
}
var i=-1
while(1)
{
    i+=1
    toast(i)
    if(i%2==0){
        加速()
    }
    弹窗检测()
    sleep(10000)
}