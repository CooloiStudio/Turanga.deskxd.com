var system = {
	win: false,
	mac: false,
	xll: false,
	ipad:false
};
//检测平台
var p = navigator.platform;
system.win = p.indexOf("Win") == 0;
system.mac = p.indexOf("Mac") == 0;
system.x11 = (p == "X11") || (p.indexOf("Linux") == 0);
system.ipad = (navigator.userAgent.match(/iPad/i) != null)?true:false;
//跳转语句
if (system.win || system.mac || system.xll) {
	$(function () {
		$(".panel").css({"height": $(window).height()});
		$.scrollify({
			section: ".panel"
		});


		$(".scroll").click(function (e) {
			e.preventDefault();
			$.scrollify("move", $(this).attr("href"));
		});
	});

	$(window).resize(function () {
		$(".panel").css({"height": $(window).height()});
		$.scrollify({
			section: ".panel"
		});


		$(".scroll").click(function (e) {
			e.preventDefault();
			$.scrollify("move", $(this).attr("href"));
		});
	});
}