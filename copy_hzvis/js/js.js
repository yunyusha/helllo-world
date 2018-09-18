Vue.component('link-img',{
    data:function () {
        return{
            style_a:{
              display:'block',
              width:'33.3%',
              background:'red',
              fontSize:'0',
              float:'left',
              overflow:'hidden',
              position:'relative',
              left:'0',
              top:'0'
            },
            style_img:{
                width:'100%',
                height:'100%',
                position:'absolute',
                left:'0',
                top:'0'
            },
            style_div:{
                zIndex:'2',
                display:'display',
                opacity:'0',
                background:'black',
                position:'absolute',
                left:'0',
                top:'0',
                width:'100%',
                fontSize:'15px',
                color:'white'
            },
            style_h1:{
                fontSize:'25px',
                marginTop: '5%',
                marginLeft:'5%'
            },
            style_div2:{
                fontSize:'18px',
                marginLeft:'5%',
                marginTop:'60%'
            }
        }
    },
    props:['datalist'],
    template:`<a href="#" @mouseenter="entera" @mouseleave="leavea" :key="datalist.url" class="yun"> 
                <div class="heimu" :style="style_div">
                    <h1 :style="style_h1">{{datalist.tit}}</h1>
                    <div class="di" :style="style_div2">
                        <p>-</p>
                        <p class="p1">{{datalist.p1}}</p>
                        <p class="p2">{{datalist.p2}}</p>
                    </div>
                </div>
                
                <img :src="datalist.url" :style="style_img" alt="">
               </a>`,
    methods: {
        entera: function (event) {
            // alert('1');
            //获取鼠标所在a标签的index值
            let s = $(event.target).index();
            // alert(s);
            s++;
            //获取图片当前高度
            let l = $(`a:nth-child(${s}) img`).width();
            let h = $(`a:nth-child(${s}) img`).height();
            console.log(l);
             $(`a:nth-child(${s}) img`).stop().animate({
                width:'110%',
                 height:'110%',
                 left:'-5%',
                 top:'-5%'
             });
            $(`a:nth-child(${s}) .heimu`).stop().animate({
                opacity:'0.5'
            });
        },
        leavea: function (event) {
            let s = $(event.target).index();
            s++;
            $(`a:nth-child(${s}) img`).stop().animate({
                left:'0',
                width:'100%',
                height:'100%',
                top:'0'
             });
            $(`a:nth-child(${s}) .heimu`).stop().animate({
                opacity:'0'
            });
        }
    }
});

//Vue部分

let vm1 =new Vue({
    el:'#root1',
    data:{
        products:[
            {'url':'images/1.jpg'},
            {'url':'images/2.jpg'},
            {'url':'images/3.jpg'},
            {'url':'images/4.jpg'},
            {'url':'images/5.jpg'},
            {'url':'images/6.jpg'},
            {'url':'images/7.jpg'},
            {'url':'images/8.jpg'},
            {'url':'images/9.jpg'},
            {'url':'images/10.jpg'}
        ]
    },
    methods: {

        enterl: function (event) {
            $('.left').stop().animate({
                left:'40px',
                width:'80px'
            });
            $('.ll').stop().animate({
                width:'60px'
            })
        },
        leavel:function (event) {
            $('.left').stop().animate({
                left:'50px',
                width:'70px'
            });
             $('.ll').stop().animate({
                width:'0'
            })
        },
            enterr: function (event) {
            $('.right').stop().animate({
                right:'40px',
                width:'80px'
            });
            $('.rr').stop().animate({
                width:'60px'
            })
        },
        leaver:function (event) {
            $('.right').stop().animate({
                right:'50px',
                width:'70px'
            });
             $('.rr').stop().animate({
                width:'0'
            })
        }
    }
});

let vm2 = new Vue({
    el:'#root2',
    data:{

        p0:"-",
         action:[
            {'url':'img/01.jpg','tit':'古茗茶饮',
                'p1':'古茗茶饮品牌升级设计',
                'p2':'品牌设计、IP设计、VI设计、品牌升级'
            },
            {'url':'img/02.jpg','tit':'每日瑜伽',
                'p1':'每日瑜伽品牌设计',
                'p2':'品牌设计、VI设计、吉祥物设计、IP设计'
            },
            {'url':'img/03.jpg','tit':'蓝小熊蓝莓',
                'p1':'蓝小熊品牌策略与设计',
                'p2':'品牌策略、品牌命名、品牌设计、VI设计、产品包装设计、网站设计'
            },
            {'url':'img/04.jpg','tit':'英树护肤品牌',
                'p1':'英树品牌全案设计',
                'p2':'品牌策划、品牌设计、VI设计、SI专卖店设计'
            },
            {'url':'img/05.gif','tit':'斑马自动售货机',
                'p1':'斑马头策略设计',
                'p2':'品牌策略、品牌命名、品牌设计、VI设计、网站设计'
            },
            {'url':'img/06.jpg','tit':'老娘舅餐饮',
                'p1':'老娘舅品牌形象升级',
                'p2':'品牌设计、VI设计、专卖店空间设计'
            },
            {'url':'img/07.jpg','tit':'甘兔庵抹茶',
                'p1':'甘兔庵品牌全案策划设计',
                'p2':'品牌策划、品牌设计、标识IP设计、专卖店设计'
            }
        ]
    }
});

// Swiper部分

var mySwiper = new Swiper('.swiper-container', {
    speed:1500,
	autoplay: {
	     disableOnInteraction: false
    }, //可选选项，自动滑动
	loop: true,
	effect:'fade',
	navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev'
    },
   pagination: {
    el: '.swiper-pagination',
    clickable: true
  }

});
for(i=0;i<mySwiper.pagination.bullets.length;i++){
  mySwiper.pagination.bullets[i].index=i;
  mySwiper.pagination.bullets[i].onmouseover=function(){
    mySwiper.slideTo(this.index+1);
  };
}
