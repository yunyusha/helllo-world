// pages/index2/index2.js
var time = null;
Page({
/**
* 页面的初始数据
*/
data: {
  focus: false,
  inPutValue:''
},
  
  bindButtonTap() {
    this.setData({
      focus: true
    })
  },
  formSubmit(e) {
    console.log(e.detail.value.input)
    var find = e.detail.value.input
    var that = this
    //console.log(focus)
    wx.request({
      url: 'http://127.0.0.1:8000/answer_sheet1/search/',
      data: {
        'file': find
      },
      header: {
        'content-type': 'application/json' // 默认值
      },
      success(res) {
        console.log(res.data)
        that.setData({
          list_data : res.data.data
        })
        console.log(find)
      }
    })
    
  },
  close: function (e) {
    this.setData({
      isRuleTrue: false
    })
  },
  goback: function (e) {
    this.setData({
      tshow: true
    })
  },
  inforRequest: function (e) {
    var that = this
    console.log(e.currentTarget.dataset.link)
    var name = e.currentTarget.dataset.link
    console.log(name)
    wx.request({
      url: 'http://127.0.0.1:8000/answer_sheet1/infor/',
      data: {
        'name': name
      },
      success(res) {
        console.log(res.data.name)
        console.log(res)
        that.setData({
          infor_data: res.data.name,
          author: res.data.author,
          isRuleTrue: true

        })

      }
    })
  },
  bindKeyInput(e) {
    this.setData({
      inputValue: e.detail.value
    })
  },
  bindReplaceInput(e) {
    const value = e.detail.value
    console.log(value)
    let pos = e.detail.cursor
    if (pos != -1) {
      // 光标在中间
      const left = e.detail.value.slice(0, pos)
      // 计算光标的位置
      pos = left.replace(/11/g, '2').length
    }

    // 直接返回对象，可以对输入进行过滤处理，同时可以控制光标的位置
    return {
      value: value.replace(/11/g, '2'),
      cursor: pos
    }
    },


//********* */
onLoad() {
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

  },
  

})