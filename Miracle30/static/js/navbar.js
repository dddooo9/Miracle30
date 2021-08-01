const triBtn = document.querySelectorAll(".triangle"),
  sublist = document.querySelectorAll(".sublist"),
  plusBtn = document.querySelector(".nav_plusBtn"),
  plusList = document.querySelector(".nav_plusList");

for (let i = 0; i < triBtn.length; i++) {
  triBtn[i].addEventListener("click", () => {
    triBtn[i].classList.toggle("clicked");
    sublist[i].classList.toggle("clicked");
  });
}

plusBtn.addEventListener("click", () => {
  plusBtn.classList.toggle("clicked");
  plusList.classList.toggle("clicked");
});
