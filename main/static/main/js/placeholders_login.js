document.addEventListener('DOMContentLoaded', (event) => {
    let fields = document.getElementsByTagName('input');
    for (let field in real_fields = Array.from(fields).slice(1, -1)) {
        real_fields[field].className += 'form-control';
    }

    real_fields[0].placeholder = 'Имя пользователя';
    real_fields[1].placeholder = 'Пароль';
    console.log(document.getElementsByClassName('outer-section')[0].style.display = 'block');
})

