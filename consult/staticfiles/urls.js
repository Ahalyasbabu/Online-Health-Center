BASE_URL = "http://127.0.0.1:9000" //change with localhost address
EHR_SERVER_URL = "http://127.0.0.1:8000" //change with localhost address

function logoutNow(){
    if(localStorage.getItem('isLogin') == 1){
        if (confirm("Are you sure want to logout?") == true) {
            localStorage.setItem('isLogin', 0)
            setTimeout(function(){
                window.location.href = BASE_URL+"/login"
            }, 200)
            
        }
    } 
    
}