function copyLink(){
    let link = document.getElementById('link');
    navigator.clipboard.writeText(link.value);
}