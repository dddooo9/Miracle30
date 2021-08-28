const btn = document.querySelectorAll(".btn"),
pTag = document.getElementsByTagName('p'),
modal = document.querySelector('.modal-body');

btn.forEach((elem, index) => {
    elem.addEventListener("click", (e) => {
        var data = pTag[index + 1].textContent;
        modal.textContent = data;
    });
});
