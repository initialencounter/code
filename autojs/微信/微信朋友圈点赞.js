// launchApp('微信')
// sleep(1000)
// id('dub').className('android.widget.TextView').text('发现').findOne().parent().parent().click()
// sleep(500)
// click(540,262)
// sleep(1000)
// // id('kn').className('android.widget.ImageView').findOne().click()
// while(1){
//     id('kn').className('android.widget.ImageView').desc('评论').findOne().click()
//     sleep(1000)
//     id('ka').findOne().click()
//     swipe(600,2000,600,100,1000)
// }
//launchApp('微信')
//sleep(1000)
// id("dub").className("android.widget.TextView").text("发现").findOne().parent().click()//发现
// id('h8z').depth('4').findOne().click()//朋友圈
// id("kn").drawingOrder('21').depth('4').className('android.widget.ImageView').findOne().click()//白点
// id('ka').findOne().click()//赞
var fri = prompt('联系人：','锦瑟思华年')
    msg = prompt('消息：',123)
id("fdi").className('android.widget.RelativeLayout').desc('搜索').drawingOrder('2').findOne().click()
sleep(1000)
id('bxz').className('android.widget.EditText').text('搜索').findOne().setText(fri)//搜索联系人
sleep(1000)
className('android.widget.RelativeLayout').drawingOrder('3').depth('2').findOne().click()//点击联系人
sleep(1000)
id('auj').className('android.widget.EditText').findOne().setText(msg)//输入消息
sleep(1000)
id('ay5').findOne().click()//发送
