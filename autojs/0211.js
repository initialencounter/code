// var a = app.getPackageName('QQ')
// log(a)
// app.launchApp('手机管家')
// sleep(10000)
// app.openAppSetting(a)
// app.editFile('/我的手机/软七八糟/口语.doc')
// app.Uninstall('QQ')
// app.launchApp('夸克').OpenUrl('www.baidu.com')
//本示例来自官方文档，是一个QQ文本消息分享脚本
// var content = rawInput('请输入要分享的文本');
// var object = rawInput('对象')
//启动QQ发送组件
// app.startActivity({
//     action: "android.intent.action'.SEND",
//     type: "text/*",
//     extras: {
//       "android.intent.extra.TEXT": content
//     },
//     packageName: "com.tencent.mobileqq",
//     className: "com.tencent.mobileqq.activity.JumpActivity"
// });
var content='123'
var qq = "000000";
// app.startActivity({ 
//     action: "android.intent.action.VIEW",
//     data:"mqq://im/chat?chat_type=wpa&version=1&src_type=web&uin=" + qq, 
//     packageName: "com.tencent.mobileqq", 
// });
var name = app.getPackageName('QQ邮箱')
sleep(1000)
// app.sendEmail({
//     email: ["10001@qq.com"],
//     subject: "这是一个邮件标题",
//     text: "这是邮件正文"
// });
// app.startActivity('settings')
// var i = app.intent({
//     action: "VIEW",
//     type: "/doc",
//     data: "file:///我的手机/软七八糟/口语.doc"
// });
// context.startActivity(i);
// app.startActivity({
//     action: "SEND",
//     type: "text/plain",
//     data: "file:///sdcard/1.txt"
// });
gestures([0, 500, [800, 300], [500, 1000]],
    [0, 500, [300, 1500], [500, 1000]]);