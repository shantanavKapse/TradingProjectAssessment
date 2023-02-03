const filename = document.querySelector("#filename");
const fileinput = document.querySelector("#csv_file");
const sub_btn = document.querySelector(".submit-btn");

fileinput.onchange = function(){
    filename.textContent = this.files[0].name;
}

sub_btn.onclick = function(){
    if (!fileinput.files[0]){
        filename.textContent = "Please provide a CSV file."
    }
}