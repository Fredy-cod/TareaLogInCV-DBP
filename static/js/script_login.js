$('.message a').click(function(){
    $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
    document.getElementById('email').value= "";
});
