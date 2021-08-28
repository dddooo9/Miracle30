const goalBtn = document.querySelector(".my_goalBtn"),
  infoBtn = document.querySelector(".my_infoBtn"),
  goal = document.querySelector(".my_goal"),
  info = document.querySelector(".my_info");

goalBtn.addEventListener("click", () => {
  goalBtn.classList.add("clicked");
  infoBtn.classList.remove("clicked");
  goal.style.display = "block";
  info.style.display = "none";
});

infoBtn.addEventListener("click", () => {
  goalBtn.classList.remove("clicked");
  infoBtn.classList.add("clicked");
  goal.style.display = "none";
  info.style.display = "block";
});
