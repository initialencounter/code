var a=0,message='新年快乐！',qq_num='2492147764';
launchApp("QQ");
id("et_search_keyword").findOne().click();
id("et_search_keyword").findOne().setText(qq_num);
sleep(1000);
id("dpr").findOne().parent().click();
while(a<1000){
    sleep(10);
    id("input").findOne().setText(message);
    id("fun_btn").findOne().click();
    a=a+1;
}