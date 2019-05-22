// pages/type/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    tshow:true
  },
  formSubmit(e) {
    console.log(e.currentTarget.dataset)
    var find = e.detail.value.input
    var that = this
    //console.log(focus)
    wx.request({
      url: 'http://127.0.0.1:8000/answer_sheet1/index/',
      data: {
        'file': find
      },
      header: {
        'content-type': 'application/json' // 默认值
      },
      success(res) {
        //console.log(res)
        that.setData({
          name: res.data
        })
        //console.log(find)
        //console.log(res)
      }
    })

  },
  inforRequest:function(e){
    var that = this
    console.log(e.currentTarget.dataset.link)
    var name = e.currentTarget.dataset.link
    console.log(name)
    wx.request({
      url: 'http://127.0.0.1:8000/answer_sheet1/infor/',
      data:{
        'name': name
      },
      success(res){
        console.log(res.data.name)
        //console.log(res)
        that.setData({
          infor_data: res.data.name,
          author:res.data.author,
          isRuleTrue: true

        })
      
      }
    })
  },
  close:function(e){
    this.setData({
      isRuleTrue: false
    })
  },
  goback:function(e){
    this.setData({
      tshow: true
    })
  },
  sendRequest:function(e){
    var that = this
    console.log(e.currentTarget.dataset.text)
    var name = e.currentTarget.dataset.text
    wx.request({
      url: 'http://127.0.0.1:8000/answer_sheet1/index/',
      data: {
        'name':name
      },
      header: {
        'content-type': 'application/json' // 默认值
      },
      success(res) {
        console.log(res.data.name)
       that.setData({
          name_data: res.data.name,
          tshow:false
          
        })
        //console.log(find)
        //console.log(res)
      }
    })
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

  }
})