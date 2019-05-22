// pages/get/index.js
var name1=''
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },
radioChange(e){
console.log(e.detail.value)
 name1 = e.detail.value
},
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
   
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    var that = this
    wx.request({
      url: 'http://127.0.0.1:8000/answer_sheet1/load/',
      data: {
      },
      header: {
        'content-type': 'application/json' // 默认值
      },
      success(res) {
        //console.log(res.data.name)
        that.setData({
          name: res.data.name
        })
      }
    })
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

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
  chooseImageTap: function () {
    var that = this;
    wx.showActionSheet({
      itemList: ['从相册中选择', '拍照'],
      itemColor: "#00000",
      success: function (res) {
        if (!res.cancel) {
          if (res.tapIndex == 0) {
            that.chooseWxImage('album')
          } else if (res.tapIndex == 1) {
            that.chooseWxImage('camera')
          }
        }
      }
    })
  },
  //本地地址路径
  chooseWxImage: function (type) {
    var that = this;
    var imgsPaths = that.data.imgs;
    wx.chooseImage({
      sizeType: ['original', 'compressed'],
      sourceType: [type],
      success: function (res) {
        let te = res.tempFilePaths[0];
        console.log(te);
        that.upImgs(te)//调用上传方法

      }
    })
  },
  //上传服务器
  upImgs: function (imgurl) {
    console.log(name1)
    var that = this;
    wx.uploadFile({
      url: 'http://127.0.0.1:8000/answer_sheet1/deal_file/',
      filePath: imgurl,
      name: 'file',
      formData: { data: name1},
      success: function (res) {
        var data = JSON.parse(res.data)
        console.log(res)
        console.log(data.answ)//接口返回网络路径;
        
      }

    })

  }
})