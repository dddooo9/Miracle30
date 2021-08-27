const option = document.querySelector(".default_option");
const select = document.querySelectorAll(".select_ul li");

option.addEventListener("click", () => {
  option.parentNode.classList.toggle("active");
});

for (let i = 0; i < select.length; i++) {
  select[i].addEventListener("click", () => {
    option.querySelector("li").outerHTML = select[i].outerHTML;
    option.parentNode.classList.toggle("active");
  });
}
