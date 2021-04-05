const chk = document.getElementById('chk');

chk.addEventListener('change', () => {
	document.body.classList.toggle('dark');
});

function save() {	
	var checkbox = document.getElementById("chk");
    localStorage.setItem("chk", checkbox.checked);	
}

//for loading
var checked = JSON.parse(localStorage.getItem("chk"));
    document.getElementById("chk").checked = checked;

