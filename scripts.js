function togglePassword(id) {
    const passwordField = document.getElementById(id);
    const icon = passwordField.nextElementSibling;
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        icon.classList.add('slash');
    } else {
        passwordField.type = 'password';
        icon.classList.remove('slash');
    }
}
