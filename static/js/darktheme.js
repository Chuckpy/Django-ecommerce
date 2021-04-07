const chk = document.getElementById('chk'); 

chk.addEventListener('change', () => {
	document.body.classList.toggle('dark');   
    save()    
});

function save() {	
	var checkbox = document.getElementById("chk");
    localStorage.setItem("chk", checkbox.checked);	
}

if (JSON.parse(localStorage.getItem("chk"))){
        document.getElementById("chk").click()           
        }
