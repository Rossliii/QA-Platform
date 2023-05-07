function bindEmailCaptchaClick(){
  $("#captcha-btn").click(function (event){
    var $this = $(this);
    event.preventDefault();

    var email = $("input[name='email']").val();
    $.ajax({
      // http://127.0.0.1:500
      // /auth/captcha/email?email=xx@qq.com
      url: "/auth/captcha/email?email="+email,
      method: "GET",
      success: function (result){
        var code = result['code'];
        if(code == 200){
          var countdown = 30;
          $this.off("click");
          var timer = setInterval(function (){
            $this.text(countdown);
            countdown -= 1;
            if(countdown <= 0){
              clearInterval(timer);
              $this.text("获取验证码");
              bindEmailCaptchaClick();
            }
          }, 1000);
          // alert("邮箱验证码发送成功！");
        }else{
          alert(result['message']);
        }
      },
      fail: function (error){
        console.log(error);
      }
    })
  });
}


// 整个网页都加载完毕后再执行的
$(function (){
  bindEmailCaptchaClick();
});