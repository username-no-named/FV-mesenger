function show_el_q(style) {
	document.querySelector("." + style).style.display = 0
	document.querySelector("." + style).style.display = "flex"
	for (var i = 0; i <= 100; i++) {
		document.querySelector("." + style).style.opacity = i
		sleep()
	}
}
function hide_el_q(style) {
	for (var i = 100; i >= 1; i--) {
		document.querySelector("." + style).style.opacity = i
		sleep()
	}
	document.querySelector("." + style).style.display = "none"
	document.querySelector("." + style).style.opacity = 0
}

function sleep() {
	for (var j = 0 ; j <= 100; j++) {}
}