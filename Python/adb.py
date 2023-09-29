a='''
/dev/input/event5: 0003 0053 00000847
/dev/input/event5: 0003 0054 00001786
/dev/input/event5: 0003 0058 00000493
/dev/input/event5: 0003 0057 00000000
/dev/input/event5: 0003 0048 00000187
/dev/input/event5: 0003 0049 00000171
/dev/input/event5: 0003 0052 00000049
/dev/input/event5: 0003 0056 00000001
/dev/input/event5: 0000 0002 00000000
/dev/input/event5: 0000 0000 00000000
'''
# b = a.replace('event7','event5')
# c = b.replace('adb','./adb')
d = a.replace('/dev','./adb shell sendevent /dev')
print(d)
#按住950，1250不动
# ./adb shell date
# ./adb shell sendevent /dev/input/event5 0001 0330 00000001
# ./adb shell sendevent /dev/input/event5 0003 0058 00000001
# ./adb shell sendevent /dev/input/event5 0003 0053 00000950
# ./adb shell sendevent /dev/input/event5 0003 0054 00001250
# ./adb shell sendevent /dev/input/event5 0000 0002 00000000
# ./adb shell sendevent /dev/input/event5 0000 0000 00000000
#
# ./adb shell sendevent /dev/input/event5 0003 0053 00000490
# ./adb shell sendevent /dev/input/event5 0003 0054 00000290
# ./adb shell sendevent /dev/input/event5 0000 0002 00000000
# ./adb shell sendevent /dev/input/event5 0000 0000 00000000
# ./adb shell sendevent /dev/input/event5 0003 0053 00000292
# ./adb shell sendevent /dev/input/event5 0003 0054 00000470
# ./adb shell sendevent /dev/input/event5 0000 0002 00000000
# ./adb shell sendevent /dev/input/event5 0003 0053 00000487
# ./adb shell sendevent /dev/input/event5 0003 0054 00000289
# ./adb shell sendevent /dev/input/event5 0000 0002 00000000