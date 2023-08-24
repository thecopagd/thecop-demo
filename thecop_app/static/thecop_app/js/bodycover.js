window.onload = () => {
    try{
        document.getElementById("body-cover").style.display="none"
    } catch {
    }
}

function openForm(b){
    document.getElementById("body-cover").style.display="block"
    document.getElementById(b).style.display="flex"
}


function closeForm(b){
    document.getElementById("body-cover").style.display="none"
    try {
        b.forEach(element => {
            document.getElementById(element).style.display="none"
        });
    } catch {

    }
}