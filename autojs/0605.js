var dy = 499+34
// function 控件判断(){
//     while(className("android.view.View").bounds(44,dy,676,dy+108).exists()){
//         dy+=34
//     }
// }
// 控件判断()
// var dy = 499
// if(className("android.view.View").bounds(44,dy,676,dy+108).exists()){
//     toast(123)
// }
// else{
//     toast(999)
// }
// toast(dy)
// if(className("android.view.View").bounds(44,dy,676,dy+108).exists()){
//     dy+=34
// }
// toast(dy)
// var a=className("android.view.View").bounds(44,dy,676,dy+108)
// a.click()
var n = className('android.widget.TextView').text('正确答案：ABC').findOne()
if(n==true){
    toast(123)
}
// 正确答案：A
// className("android.view.View").text("正确答案：ABC").findOne()
// B
// C
// D 
// AB 
// AC
// AD
// BC 
// BD 
// CD
// ABC
// ABD 
// ACD 
// BCD
// ABCD 
