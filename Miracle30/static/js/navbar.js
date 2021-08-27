const triBtn = document.querySelectorAll(".triangle"),
  sublist = document.querySelectorAll(".sublist");

for (let i = 0; i < triBtn.length; i++) {
  triBtn[i].addEventListener("click", () => {
    triBtn[i].classList.toggle("clicked");
    sublist[i].classList.toggle("clicked");
  });
}
