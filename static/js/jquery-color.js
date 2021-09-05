$('#click_advance').click(function() {
    var theme = localStorage.getItem("theme");
    if (theme == "dark") {
      // localStorage.setItem("theme","light");

      localStorage.setItem("theme","light");
      $("body").toggleClass( "light-mode" );
      $("body").removeClass( "dark-mode" );

    }

    else {
      localStorage.setItem("theme","dark");
      $("body").toggleClass( "dark-mode" );
    }

    // localStorage.setItem("theme","light");
    // $("body").toggleClass('dark-mode');
    // $(this).toggleClass("fa-sun-o fa-moon-o");
});

var theme = localStorage.getItem("theme");
if (theme == "dark") {
  // localStorage.setItem("theme","light");
  $("#click_advance").toggleClass( "active" )
  $("body").toggleClass( "dark-mode" );
  $("body").removeClass('light-mode');
}
if (theme == "light") {
  $("#click_advance").removeClass( "active" )
  $("body").removeClass( "dark-mode" );
  $("body").toggleClass('light-mode');
}


// $('#click_advance').click(function() {
// 		$("body").toggleClass('dark-mode');
//     // $(this).toggleClass("fa-sun-o fa-moon-o");
// });
