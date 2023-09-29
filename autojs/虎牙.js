var sh = new Shell(true) 
app.startActivity({
    action : 'VIEW',
    packageName : 'com.duowan.kiwi',
    className : 'com.duowan.kiwi.homepage.Homepage',
    root : true
})
id('search_ll').depth('14').click()
id('search_content').depth('8').findOne().setText('31520')
id('search_btn').findOne().click()
waitForActivity('com.duowan.kiwi.liveroom.ChannelPage', 50)
sleep(2000)
sh.exec('input tap 500 400')
sleep(200)
id('full_screen').findOne().click()
sleep(100)

sh.exit()