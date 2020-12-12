const btnDelete= document.querySelectorAll('.btn-delete')


if(btnDelete){
    const btnArry= Array.from(btnDelete);
    btnArry.forEach((btn) => {
        btn.addEventListener('click', (e) =>{
            if(!confirm('Are you sure you wnat delete it?')) {
                e.preventDefault();
            }
        });
    });
}