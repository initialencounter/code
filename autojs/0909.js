var arr = files.listDir('/storage/emulated/0/Download/149790/ts')
// arr.sort()
log(arr)
//按下
setevent /dev/input/event7: 0001 014a 00000001
/dev/input/event7: 0003 003a 00000001
/dev/input/event7: 0003 0035 00000122
/dev/input/event7: 0003 0036 000001d5
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0000 0000 00000000

//松开
/dev/input/event7: 0001 014a 00000000
/dev/input/event7: 0003 003a 00000000
/dev/input/event7: 0003 0035 00000122
/dev/input/event7: 0003 0036 000001d5
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0000 0000 00000000

//滑动过程中
/dev/input/event7: 0003 0035 00000225
/dev/input/event7: 0003 0036 000003ba
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0000 0000 00000000

/dev/input/event7: 0003 0035 00000225
/dev/input/event7: 0003 0036 000003bb
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0000 0000 00000000

//松开
/dev/input/event7: 0001 014a 00000000
/dev/input/event7: 0003 003a 00000000
/dev/input/event7: 0003 0035 00000225
/dev/input/event7: 0003 0036 000003bb
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0000 0000 00000000

//模拟双指缩放
//genymotion在mac下是通过摁下control然后拖动鼠标来模拟向外滑动，向内滑动等操作，用sendevent可以不用加上control的操作
//摁下control
/dev/input/event7: 0001 007d 00000001
/dev/input/event7: 0000 0000 00000000

//鼠标左键摁下
/dev/input/event7: 0001 014a 00000001
/dev/input/event7: 0003 003a 00000001

//一组
/dev/input/event7: 0003 0035 00000144
/dev/input/event7: 0003 0036 00000280
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0003 0035 00000000
/dev/input/event7: 0003 0036 00000280
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0000 0000 00000000

/dev/input/event7: 0003 0035 00000001
/dev/input/event7: 0003 0036 00000280
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0003 0035 00000143
/dev/input/event7: 0003 0036 00000280
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0000 0000 00000000

/dev/input/event7: 0003 0035 00000001
/dev/input/event7: 0003 0036 00000280
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0003 0035 00000143
/dev/input/event7: 0003 0036 00000280
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0000 0000 00000000

/dev/input/event7: 0003 0035 00000001
/dev/input/event7: 0003 0036 0000027f
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0003 0035 00000143
/dev/input/event7: 0003 0036 0000027f
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0000 0000 00000000

/dev/input/event7: 0003 0035 00000002
/dev/input/event7: 0003 0036 0000027f
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0003 0035 00000142
/dev/input/event7: 0003 0036 0000027f
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0000 0000 00000000

/dev/input/event7: 0003 0035 00000003
/dev/input/event7: 0003 0036 0000027f
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0003 0035 00000141
/dev/input/event7: 0003 0036 0000027f
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0000 0000 00000000

//松开鼠标左键
/dev/input/event7: 0001 014a 00000000
/dev/input/event7: 0003 003a 00000000
/dev/input/event7: 0000 0002 00000000
/dev/input/event7: 0000 0000 00000000

//松开control
/dev/input/event7: 0001 007d 00000000
/dev/input/event7: 0000 0000 00000000
./adb shell sendevent /dev/input/event5 0001 0330 00000001
./adb shell sendevent /dev/input/event5 0003 0058 00000001
./adb shell sendevent /dev/input/event5 0003 0053 00000345
./adb shell sendevent /dev/input/event5 0003 0054 00000834
./adb shell sendevent /dev/input/event5 0000 0002 00000000
./adb shell sendevent /dev/input/event5 0003 0053 00000490
./adb shell sendevent /dev/input/event5 0003 0054 00000290
./adb shell sendevent /dev/input/event5 0000 0002 00000000
./adb shell sendevent /dev/input/event5 0000 0000 00000000
./adb shell sendevent /dev/input/event5 0003 0053 00000292
./adb shell sendevent /dev/input/event5 0003 0054 00000470
./adb shell sendevent /dev/input/event5 0000 0002 00000000
./adb shell sendevent /dev/input/event5 0003 0053 00000487
./adb shell sendevent /dev/input/event5 0003 0054 00000289
./adb shell sendevent /dev/input/event5 0000 0002 00000000
./adb shell sendevent /dev/input/event5 0000 0000 00000000
