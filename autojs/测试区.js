
threads.start(function () {
    var beginBtn;
        if (beginBtn = classNameContains("Button").textContains("立即开始").findOne(2000)) {
            beginBtn.click();
        }
    })
if(!requestScreenCapture()){
    toast("请求截图失败");
    exit
}
sleep(250)
// var imsge = captureScreen()
// var temp = images.clip(imsge, 178, 205, 30, 30)
// images.save(temp, '/storage/emulated/0/脚本/局内操作/小头像.jpg', 'jpg', 100)
captureScreen('./img.jpg')
var img = images.read('./img.jpg')
log(colors.blue(images.pixel(img,144,205))+'前')  
var temp = images.read('/storage/emulated/0/脚本/局内操作/小地图头像.jpg')
var res = findImage(img, temp,{
    region: [0, 0, 500, 500],
    threshold: 0.5
})
log(res)
// img.recycle()
// var img = images.read('./img.jpg')
log(colors.blue(images.pixel(img,144,205))+'后')
temp.recycle()
log((colors.blue(images.pixel(img,144,205)))-22<5)

if((colors.blue(images.pixel(img,144,205)))-22<5){//小狼刷新
    img.recycle()
    log(res)
    log(Math.abs((res.x)-144))
    log(Math.abs((res.y)-205))
    var a=1
    while(a){
        if(Math.abs(res.x+20-144)>10){
            if(Math.abs(res.y-205)>10){
                if(res.x+20<144){
                    if(Math.abd(res.y-186)<10){
                        if(res.y>202|res.y<186){
                            swipe(345,845,645,845,1000)//右
                        } 
                    }
                }
                                       
            }else if(res.x+20>144){
                swipe(345,845,45,845,1000)//左
            };
            if(res.y+20>205){
                swipe(345,845,345,545,1000)//上
            }else if(res.y+20<205){
                swipe(345,845,345,1145,1000)//下
            };        
        }else if(Math.abs(res.y-205)>10){
            if(res.y+20>205){
                swipe(345,845,345,545,1000)//上
            }else if(res.y+20<205){
                swipe(345,845,345,1145,1000)//下
            }; 
        }else{
            a = 0
        }
        captureScreen('./img.jpg')
            var img = images.read('./img.jpg')
            var temp = images.read('/storage/emulated/0/脚本/局内操作/小地图头像.jpg')
            var res = findImage(img, temp,{
                region: [0, 0, 500, 500],
            threshold: 0.5
            })
            img.recycle()
            temp.recycle()
            log(res)

    }


    // while(Math.abs(res.x+20-144)>10 & Math.abs(res.y-205)>10){//| 
    //     if(res.x+20<144){
    //         swipe(345,845,645,845,1000)//右
    //     }else if(res.x+20>144){
    //         swipe(345,845,45,845,1000)//左
    //     };
    //     if(res.y+20>205){
    //         swipe(345,845,345,545,1000)//上
    //     }else if(res.y+20<205){
    //         swipe(345,845,345,1145,1000)//下
    //     };
        
    //     captureScreen('./img.jpg')
    //     var img = images.read('./img.jpg')
    //     var temp = images.read('/storage/emulated/0/脚本/局内操作/小地图头像.jpg')
    //     var res = findImage(img, temp,{
    //         region: [0, 0, 500, 500],
    //         threshold: 0.5
    //     })
    //     img.recycle()
    //     temp.recycle()
    //     log(res)
    // }
    // while(Math.abs(res.y+20-205)>10){//| Math.abs(res.y-205)>10
    //     if(res.y+20>205){
    //         swipe(345,845,345,545,1000)//上
    //     }else if(res.y+20<205){
    //         swipe(345,845,345,1145,1000)//下
    //     };
    //     captureScreen('./img.jpg')
    //     var img = images.read('./img.jpg')
    //     var temp = images.read('/storage/emulated/0/脚本/局内操作/小地图头像.jpg')
    //     var res = findImage(img, temp,{
    //         region: [0, 0, 500, 500],
    //         threshold: 0.5
    //     })
    //     img.recycle()
    //     temp.recycle()
    //     log(res)
    // }
    

}
function xfx(res){
    if(res.x<144){
        swipe(345,845,445,845,1000)
    }else if(res.x>144){
        swipe(345,845,245,845,1000)
    }
}
function yfx(res){
    if(res.y<205){
        swipe(345,845,345,745,1000)
    }else if(res.y<205){
        swipe(345,845,345,645,1000)
    }

}
function yid(){
var a=1
while(a){
    if(Math.abs(res.x+20-144)>10){
        if(Math.abs(res.y-205)>10){
            if(res.x+20<144){
                swipe(345,845,645,845,1000)//右
            }else if(res.x+20>144){
                swipe(345,845,45,845,1000)//左
            };
            if(res.y+20>205){
                swipe(345,845,345,545,1000)//上
            }else if(res.y+20<205){
                swipe(345,845,345,1145,1000)//下
            };        
        }
    }else if(Math.abs(res.y-205)>10){
        if(res.y+20>205){
            swipe(345,845,345,545,1000)//上
        }else if(res.y+20<205){
            swipe(345,845,345,1145,1000)//下
        }; 
    }else{
        a = 0
    }
    captureScreen('./img.jpg')
        var img = images.read('./img.jpg')
        var temp = images.read('/storage/emulated/0/脚本/局内操作/小地图头像.jpg')
        var res = findImage(img, temp,{
            region: [0, 0, 500, 500],
            threshold: 0.5
        })
        img.recycle()
        temp.recycle()
        log(res)

}
}