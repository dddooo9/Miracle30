// modal 창 띄우기
const modal = document.getElementById("myModal"),
  modalBtn = document.querySelectorAll(".btn"), // 버튼 누르면 모달버튼 뜸
  closeBtn = document.querySelector(".close");

// modalBtn.onclick = function () {
//   modal.style.display = "block";
// };

closeBtn.onclick = function () {
  modal.style.display = "none";
};

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

// 데이터 넣기
// const btn = document.querySelectorAll(".btn"),
const pTag = document.getElementsByTagName("p"),
  modalBody = document.querySelector(".modal-body");

modalBtn.forEach((elem, index) => {
  elem.addEventListener("click", (e) => {
    console.log(elem, index);
    modal.style.display = "block";
    let data = pTag[index].textContent;
    data = data.replace(/'/gi, "");
    data = data.substr(1, data.length - 2);
    modalBody.textContent = data;
  });
});


const certifyBtn = document.querySelector(".btn1");

certifyBtn.addEventListener("click", (e) => {
    if(tryCertify()) e.preventDefault();
})

function tryCertify(){
    return !confirm(`인증은 한번 등록하면 수정/삭제할 수 없습니다.`);
}