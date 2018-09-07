Vue.component('link-img',{
    data:function () {
        return{
            style_img:{},
            style_div:{}
        }
    },
    props:['datalist'],
    template:`<a href="#" :stlye="style_img" v-for="item in datalist"> 
                <div :style_div></div>
                <img src="" alt="">
               </a>`
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