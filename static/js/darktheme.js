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

        (function(d, s, id) {
            var js, fjs = d.getElementsByTagName(s)[0];
            if (d.getElementById(id)) return;
            js = d.createElement(s); js.id = id;
            js.src = "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0";
            fjs.parentNode.insertBefore(js, fjs);
            }(document, 'script', 'facebook-jssdk'));

