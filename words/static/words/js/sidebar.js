function toggleSidebar(){
    document.getElementById("sidebar").classList.toggle('active');
}


document.addEventListener('DOMContentLoaded', function() {
    const btn = document.getElementsByClassName("label")[0];
    const email = document.getElementsByClassName("email")[0];

    btn.disabled = true;

    email.onkeyup = () => {
        if (email.value.length > 0) {
            btn.disabled = false;
        } else {
            btn.disabled = true;
        }
    }
});
