
Page({

  data:{
    imgs:[],//本地图片地址数组
    picPaths:[],//网络路径
    items:[
      {name:'A'},
      {name:'B'},
      {name:'C'},
      {name:'D'}
    ]
  },
  formSubmit(e) {
    var img = e.detail.value;
    console.log(img)
    wx.request({
      url: 'http://127.0.0.1:8000/answer_sheet1/save/',
      data: {
        'data':img,
        'name': img.input
      },
      header: {
        'content-type': 'application/json' // 默认值
      },
      success(res) {
        console.log(res)
      
      }
    })
  },
  saveRequest(e) {
    // var img = e.detail;
    // console.log(img)
  },

  onLoad() {
          this.ctx = wx.createCameraContext();
    var arrl = new Array(25);
    for (var i = 0; i < arrl.length; i++) {
      arrl[i] = i;
    }
    this.setData({
      changes:arrl
    })
  },
  takePhoto() {
    this.ctx.takePhoto({
      quality: 'high',
      success: (res) => {
        this.setData({
          src: res.tempImagePath
        })
      }
    })
  },

  error(e) {
    console.log(e.detail)
  },
  //添加上传图片
  chooseImageTap:function(){
    var that = this;
    wx.showActionSheet({
      itemList:['从相册中选择','拍照'],
      itemColor:"#00000",
      success:function (res) {
        if(!res.cancel){
          if (res.tapIndex == 0) {
            that.chooseWxImage('album')
          }else if (res.tapIndex == 1) {
            that.chooseWxImage('camera')
          }
        }
      }
    })
  },
  //本地地址路径
  chooseWxImage:function(type){
    var that = this;
    var imgsPaths = that.data.imgs;
    wx.chooseImage({
      sizeType:['original','compressed'],
      sourceType:[type],
      success:function (res) {
        let te = res.tempFilePaths[0];
        console.log(te);
        that.upImgs(te)//调用上传方法

      }
    })
  },
  //上传服务器
  upImgs:function (imgurl) {
    var that = this;
    wx.uploadFile({
      url:'http://127.0.0.1:8000/answer_sheet1/deal_file/',
      filePath:imgurl,
      name:'file',
      formData:null,
      success:function (res) {
        var data = JSON.parse(res.data)
        console.log(data.answ)//接口返回网络路径;
      }

    })

  }

})
