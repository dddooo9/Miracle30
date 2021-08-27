const goalAdd = document.querySelector(".btn1"),
  cash = document.querySelector("#cash");

goalAdd.addEventListener("click", (e) => {
    if(parseInt(cash.textContent) < 500){
        console.log("cash")
        alert("그룹을 생성하기 위해서는 500별 이상이 필요합니다.");
        e.preventDefault();
    }
});